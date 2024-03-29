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
from .forms import ReviewForm
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages







def homepage(request):
	data = cartData(request)
	data2 = wishlistData(request)

	# wishlists and carts counts
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists_counts = data2['wishlists_counts']


	##########   products types   ####################
	#1. most liked
	most_liked = Product.objects.order_by('-id')[0:8]
	most = list(most_liked)
	shuffle(most)
	final = most

	#2. best seller
	best_seller = Product.objects.order_by('name')[0:8]
	best = list(best_seller)
	shuffle(best)
	final = best

	#3. hot trend
	hot_trend = Product.objects.order_by('name')[8:16]
	hot = list(hot_trend)
	shuffle(hot)
	final = hot

	#new products
	new_products_w = Product.objects.filter(category__name='WomensFashions').order_by('-id')[:8]
	new_w = list(new_products_w)
	shuffle(new_w)
	final = new_w

	new_products_m = Product.objects.filter(category__name='MensFashions').order_by('-id')[:8]
	new_m = list(new_products_m)
	shuffle(new_m)
	final = new_m

	new_products_a = Product.objects.filter(category__name='Accessories').order_by('-id')[:12]
	new_a = list(new_products_a)
	shuffle(new_a)
	final = new_a

	new_products_k = Product.objects.filter(category__name='KidsFashions').order_by('-id')[:8]
	new_k = list(new_products_k)
	shuffle(new_k)
	final = new_k
	
	# categories products
	womens_fashions = Product.objects.filter(category__name='WomensFashions').count()
	mens_fashions = Product.objects.filter(category__name='MensFashions').count()
	kids_fashions = Product.objects.filter(category__name='KidsFashions').count()
	cosmetics = Product.objects.filter(category__name='Cosmetics').count()
	accessories = Product.objects.filter(category__name='Accessories').count()




	kids_products = Product.objects.filter(category__name='KidsFashions')[:8]
	kids = list(kids_products)
	shuffle(kids)
	final = kids



	womens_products = Product.objects.filter(category__name='WomensFashions')[:8]
	womens = list(womens_products)
	shuffle(womens)
	final = womens







	template_name = 'store/homepage.html'
	context = {
		
		'new_w':new_w,
		'new_m':new_m,
		'new_k':new_k,
		'new_a':new_a,
		'items':items,
		'order':order,
		'cartItems':cartItems,
		'wishlists_counts':wishlists_counts,
		'most':most,
		'best':best,
		'hot':hot,
		'womens_fashions':womens_fashions,
		'mens_fashions':mens_fashions,
		'kids_fashions':kids_fashions,
		'cosmetics':cosmetics,
		'accessories':accessories,
		'kids':kids,
		'womens':womens

		
		}
	return render(request,template_name, context)



def cart(request):
	data = cartData(request)
	data2 = wishlistData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists_counts = data2['wishlists_counts']



	template_name = 'store/cart.html'
	context = {

		'items':items, 
		'order':order, 
		'cartItems':cartItems,
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




	template_name = 'store/checkout.html'
	context = {

		'items':items, 
		'order':order, 
		'cartItems':cartItems,
		'wishlists_counts':wishlists_counts
	
		
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
		phone=data['shipping']['phone'],

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


	query1 =  request.GET.get('product')

	search_results = Product.objects.filter( 
			Q(category__name__icontains=query1) |  Q(name__icontains=query1) | Q(sub_category__icontains=query1)
			)



	template_name = 'store/search_results.html'
	context = {
		'search_results':search_results,
		'query1':query1 , 
		'cartItems':cartItems,
		'items':items,
		'order':order,
		'wishlists_counts':wishlists_counts
		}
	return render(request,template_name, context)




# new


def womensFashions(request):
	data = cartData(request)
	data2 = wishlistData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists_counts = data2['wishlists_counts']

	
	shoes = Product.objects.filter(category__name='WomensFashions').filter(sub_category='Shoes')
	clothes = Product.objects.filter(category__name='WomensFashions').filter(sub_category='Clothes')
	handbags = Product.objects.filter(category__name='WomensFashions').filter(sub_category='Handbags')


	template_name = 'store/womens_fashions.html'
	context = {
		'cartItems':cartItems,
		'items':items,
		'order':order,
		'wishlists_counts':wishlists_counts,
		'shoes':shoes,
		'clothes':clothes,
		'handbags':handbags
	}
	return render(request,template_name,context)




def mensFashions(request):
	data = cartData(request)
	data2 = wishlistData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists_counts = data2['wishlists_counts']

	
	shoes = Product.objects.filter(category__name='MensFashions').filter(sub_category='Shoes')
	clothes = Product.objects.filter(category__name='MensFashions').filter(sub_category='Clothes')
	sutes = Product.objects.filter(category__name='MensFashions').filter(sub_category='Sutes')
	shirts = Product.objects.filter(category__name='MensFashions').filter(sub_category='Shirts')
	tshirts = Product.objects.filter(category__name='MensFashions').filter(sub_category='TShirts')
	jeans = Product.objects.filter(category__name='MensFashions').filter(sub_category='Jeans')




	template_name = 'store/mens_fashions.html'
	context = {
		'cartItems':cartItems,
		'items':items,
		'order':order,
		'wishlists_counts':wishlists_counts,
		'shoes':shoes,
		'clothes':clothes,
		'sutes':sutes,
		'shirts':shirts,
		'tshirts':tshirts,
		'jeans':jeans
	}
	return render(request,template_name,context)




def kidsFashions(request):
	data = cartData(request)
	data2 = wishlistData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists_counts = data2['wishlists_counts']

	

	shoes = Product.objects.filter(category__name='KidsFashions').filter(sub_category='Shoes')
	clothes = Product.objects.filter(category__name='KidsFashions').filter(sub_category='Clothes')
	dresses = Product.objects.filter(category__name='KidsFashions').filter(sub_category='Dresses')
	sutes = Product.objects.filter(category__name='KidsFashions').filter(sub_category='Sutes')



	template_name = 'store/kids_fashions.html'
	context = {
		'cartItems':cartItems,
		'items':items,
		'order':order,
		'wishlists_counts':wishlists_counts,
		'shoes':shoes,
		'clothes':clothes,
		'dresses':dresses,
		'sutes':sutes
	}
	return render(request,template_name,context)




def cosmetics(request):
	data = cartData(request)
	data2 = wishlistData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists_counts = data2['wishlists_counts']

	
	categories = Category.objects.all()
	cosmetics = Product.objects.filter(category__name='Cosmetics')


	template_name = 'store/cosmetics.html'
	context = {
		'cartItems':cartItems,
		'items':items,
		'order':order,
		'categories':categories,
		'cosmetics':cosmetics,
		'wishlists_counts':wishlists_counts
	}
	return render(request,template_name,context)




def accessories(request):
	data = cartData(request)
	data2 = wishlistData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists_counts = data2['wishlists_counts']

	
	phones = Product.objects.filter(category__name='Accessories').filter(sub_category='Phones')




	template_name = 'store/accessories.html'
	context = {
		'cartItems':cartItems,
		'items':items,
		'order':order,
		'wishlists_counts':wishlists_counts,
		'phones':phones
	}
	return render(request,template_name,context)


def shop(request):
	data = cartData(request)
	data2 = wishlistData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	wishlists_counts = data2['wishlists_counts']

	accessories_products = Product.objects.filter(category__name='Accessories')
	men_products = Product.objects.filter(category__name='MensFashions')
	women_products = Product.objects.filter(category__name='WomensFashions')
	kids_products = Product.objects.filter(category__name='KidsFashions')
	cosmetics_products = Product.objects.filter(category__name='Cosmetics')




	context = {
		'cartItems':cartItems,
		'items':items,
		'order':order,
		'wishlists_counts':wishlists_counts,
		'accessories_products':accessories_products,
		'men_products':men_products,
		'women_products':women_products,
		'kids_products':kids_products,
		'cosmetics_products':cosmetics_products
		
		}

	return render(request, 'store/shop.html',context)