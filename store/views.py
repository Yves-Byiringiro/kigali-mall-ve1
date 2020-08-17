from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, wishlistData, guestOrder
from random import shuffle
from about.models import *
from django.views.generic import ListView
from django.db.models import Q
from .forms import ReviewForm,MomoTranctionIDForm
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages




def homepage(request):
	return render(request,'store/homepage.html')


# def homepage(request):
# 	data = cartData(request)
# 	data2 = wishlistData(request)

# 	cartItems = data['cartItems']
# 	order = data['order']
# 	items = data['items']
# 	wishlists_counts = data2['wishlists_counts']

# 	products = Product.objects.order_by('-id')
# 	top_selling = Product.objects.order_by('name')
# 	top = list(top_selling)
# 	shuffle(top)
# 	final = top

# 	most_liked = Product.objects.order_by('id')
# 	most = list(most_liked)
# 	shuffle(most)
# 	final = most

# 	new_products = products[:20]
# 	new = list(new_products)
# 	shuffle(new)
# 	final = new
# 	categories = Category.objects.all()

# 	new_products_cat = products[0:3]
# 	new_products_cat2 = products[3:7]

# 	top_selling_cat = top_selling[0:3]
# 	top_selling_cat2 = top_selling[3:7]

# 	most_liked_cat = most_liked[0:3]
# 	most_liked_cat2 = most_liked[3:7]
	


# 	active_carousels = ActiveCarousel.objects.all()
# 	carousels = Carousel.objects.all()



# 	template_name = 'store/homepage.html'
# 	context = {
# 		'products':products, 
# 		'new':new, 
# 		'items':items,
# 		'order':order,
# 		'cartItems':cartItems,
# 		'categories':categories,
# 		'new_products_cat':new_products_cat,
# 		'new_products_cat2':new_products_cat2,
# 		'top':top,
# 		'top_selling_cat':top_selling_cat,
# 		'top_selling_cat2':top_selling_cat2,
# 		'most':most,
# 		'most_liked_cat':most_liked_cat,
# 		'most_liked_cat2':most_liked_cat2,
# 		'carousels':carousels,
# 		'active_carousels':active_carousels,
# 		'wishlists_counts':wishlists_counts

# 		}
# 	return render(request,template_name, context)



def cart(request):
	data = cartData(request)
	data2 = wishlistData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists_counts = data2['wishlists_counts']

	categories = Category.objects.all()


	template_name = 'store/cart.html'
	context = {

		'items':items, 
		'order':order, 
		'cartItems':cartItems,
		'categories':categories,
		'wishlists_counts':wishlists_counts
		
		}
	return render(request, template_name, context)



def checkout(request):
	data = cartData(request)
	data2 = wishlistData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists_counts = data2['wishlists_counts']

	categories = Category.objects.all()
	


	template_name = 'store/checkout.html'
	context = {

		'items':items, 
		'order':order, 
		'cartItems':cartItems,
		'categories':categories,
		'wishlists_counts':wishlists_counts,
		
		}
	return render(request, template_name, context)




def updateItems(request):
	data = json.loads(request.body)

	productId = data['productId']
	action = data['action']

	customer = request.user
	product = Product.objects.get(id=productId)
	wishlist, created = Wishlist.objects.get_or_create(customer=customer, product=product)

	return JsonResponse('Item added to wishlist', safe=False)


def destroy_wishlist(request):
	data = json.loads(request.body)

	productId = data['productId']
	action = data['action']

	customer = request.user
	product = Product.objects.get(id=productId)

	wishlist_destroy = Wishlist.objects.get(customer=customer,product=product)

	wishlist_destroy.delete()
	return JsonResponse('Wishlist item removed', safe=False)



def wishlist(request):
	data = cartData(request)
	data2 = wishlistData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists = data2['wishlists']
	wishlists_counts = data2['wishlists_counts']


	categories = Category.objects.all()


	# wishlist = json.loads(request.COOKIES['wishlist'])

	template_name = 'store/wishlist.html'

	context = {

		'items':items, 
		'order':order, 
		'cartItems':cartItems,
		'categories':categories,
		'wishlists':wishlists,
		'wishlists_counts':wishlists_counts
	}
	return render(request, template_name, context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']


	customer = request.user
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)



def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		country=data['shipping']['country'],
		)

	return JsonResponse('Payment submitted..', safe=False)



def productDetails(request,slug):
	data = cartData(request)
	data2 = wishlistData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists_counts = data2['wishlists_counts']

	
	categories = Category.objects.all()
	product = get_object_or_404(Product, slug=slug)



	images = ProductImage.objects.filter(product=product)
	related_products = Product.objects.filter(category=product.category).exclude(name=product.name)[:4]
	my_list = list(related_products)
	shuffle(my_list)
	final = my_list

	reviews = Review.objects.filter(product=product, published=True)
	page = request.GET.get('page', 1)
	
	paginator = Paginator(reviews, 4)
	try:
		reviews = paginator.page(page)
	except PageNotAnInteger:
		reviews = paginator.page(1)
	except EmptyPage:
		reviews = paginator.page(paginator.num_pages)

	if request.method == 'POST':
		review_form = ReviewForm(request.POST)
		if review_form.is_valid():
			review = review_form.save(commit=False)
			review.product = product
			review.save()
	review_form  = ReviewForm()

	template_name = 'store/product_details.html'
	context = {
		'product':product,
		'images':images,
		'my_list':my_list,
		'cartItems':cartItems,
		'items':items,
		'order':order,
		'categories':categories,
		'review_form':review_form,
		'reviews':reviews,
		'wishlists_counts':wishlists_counts
	}
	return render(request,template_name,context)



def productResults(request):
	data = cartData(request)
	data2 = wishlistData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists_counts = data2['wishlists_counts']


	query1 =  request.GET.get('category_name')
	query2 =  request.GET.get('product')
	search_results = Product.objects.filter( 
			Q(category__name__iexact=query1) &  Q(name__icontains=query2)
			)
	categories = Category.objects.all()



	template_name = 'store/search_results.html'
	context = {
		'search_results':search_results,
		'cartItems':cartItems,
		'items':items,
		'order':order,
		'categories':categories,
		'query2':query2,
		'query1':query1,
		'wishlists_counts':wishlists_counts
		}
	return render(request,template_name, context)



# def laptops(request):
# 	data = cartData(request)
# 	data2 = wishlistData(request)

# 	cartItems = data['cartItems']
# 	order = data['order']
# 	items = data['items']
# 	wishlists_counts = data2['wishlists_counts']

# 	categories = Category.objects.all()
# 	laptops = Product.objects.filter(category__name='Laptops')



# 	template_name = 'store/laptops.html'
# 	context = {
# 		'cartItems':cartItems,
# 		'items':items,
# 		'order':order,
# 		'categories':categories,
# 		'laptops':laptops,
# 		'wishlists_counts':wishlists_counts
# 	}
# 	return render(request,template_name,context)


def smartphones(request):
	data = cartData(request)
	data2 = wishlistData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists_counts = data2['wishlists_counts']

	
	categories = Category.objects.all()
	smartphones = Product.objects.filter(category__name='Smartphones')



	template_name = 'store/smartphones.html'
	context = {
		'cartItems':cartItems,
		'items':items,
		'order':order,
		'categories':categories,
		'smartphones':smartphones,
		'wishlists_counts':wishlists_counts
	}
	return render(request,template_name,context)



# def cameras(request):
# 	data = cartData(request)
# 	data2 = wishlistData(request)

# 	cartItems = data['cartItems']
# 	order = data['order']
# 	items = data['items']
# 	wishlists_counts = data2['wishlists_counts']

	
# 	categories = Category.objects.all()
# 	cameras = Product.objects.filter(category__name='Cameras')



# 	template_name = 'store/cameras.html'
# 	context = {
# 		'cartItems':cartItems,
# 		'items':items,
# 		'order':order,
# 		'categories':categories,
# 		'cameras':cameras,
# 		'wishlists_counts':wishlists_counts
# 	}
# 	return render(request,template_name,context)



# def accessories(request):
# 	data = cartData(request)
# 	data2 = wishlistData(request)

# 	cartItems = data['cartItems']
# 	order = data['order']
# 	items = data['items']
# 	wishlists_counts = data2['wishlists_counts']

	
# 	categories = Category.objects.all()
# 	accessories = Product.objects.filter(category__name='Accessories')



# 	template_name = 'store/accessories.html'
# 	context = {
# 		'cartItems':cartItems,
# 		'items':items,
# 		'order':order,
# 		'categories':categories,
# 		'accessories':accessories,
# 		'wishlists_counts':wishlists_counts
# 	}
# 	return render(request,template_name,context)



def bags(request):
	data = cartData(request)
	data2 = wishlistData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists_counts = data2['wishlists_counts']

	
	categories = Category.objects.all()
	bags = Product.objects.filter(category__name='Bags')



	template_name = 'store/bags.html'
	context = {
		'cartItems':cartItems,
		'items':items,
		'order':order,
		'categories':categories,
		'bags':bags,
		'wishlists_counts':wishlists_counts
	}
	return render(request,template_name,context)



def shoes(request):
	data = cartData(request)
	data2 = wishlistData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists_counts = data2['wishlists_counts']

	
	categories = Category.objects.all()
	shoes = Product.objects.filter(category__name='Shoes')



	template_name = 'store/shoes.html'
	context = {
		'cartItems':cartItems,
		'items':items,
		'order':order,
		'categories':categories,
		'shoes':shoes,
		'wishlists_counts':wishlists_counts
	}
	return render(request,template_name,context)



def home_furnitures(request):
	data = cartData(request)
	data2 = wishlistData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists_counts = data2['wishlists_counts']

	
	categories = Category.objects.all()
	home_furnitures = Product.objects.filter(category__name='Furnitures')


	template_name = 'store/home_furnitures.html'
	context = {
		'cartItems':cartItems,
		'items':items,
		'order':order,
		'categories':categories,
		'home_furnitures':home_furnitures,
		'wishlists_counts':wishlists_counts
	}
	return render(request,template_name,context)



def payMobilemoney(request):
	data = cartData(request)
	data2 = wishlistData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists_counts = data2['wishlists_counts']

	
	categories = Category.objects.all()
	momo = Mymomo.objects.get(pk=1)
	
	
	if request.method == 'POST':
		form = MomoTranctionIDForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your Transaction ID has been submitted successfully !.')
			return redirect('homepage')
	form  = MomoTranctionIDForm()

	template_name = 'store/pay_mobilemoney.html'

	context = {
		'cartItems':cartItems,
		'items':items,
		'order':order,
		'categories':categories,
		'wishlists_counts':wishlists_counts,
		'momo':momo,
		'form':form
	}
	return render(request, template_name, context)