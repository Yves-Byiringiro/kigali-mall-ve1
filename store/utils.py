import json
from .models import *

from django.conf import settings

User = settings.AUTH_USER_MODEL




def cookieWishlist(request):
	#Create empty wishlist for now for non-logged in user
	try:
		wishlist = json.loads(request.COOKIES['wishlist'])
	except:
		wishlist = {}
	
	wishlists = []
	wishlists_counts = 0

	for i in wishlist:
		wishlists_counts += wishlist[i]['quantity']

		product = Product.objects.get(id=i)

		item = {
			'id':product.id,
			'product':{'id':product.id,'name':product.name, 'price':product.price, 
			'main_image':product.main_image},
		}
		wishlists.append(item)

	return {'wishlists':wishlists,'wishlists_counts':wishlists_counts}


def cookieCart(request):

	#Create empty cart for now for non-logged in user
	try:
		cart = json.loads(request.COOKIES['cart'])
	except:
		cart = {}
		# print('CART:', cart)

	items = []
	order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
	cartItems = order['get_cart_items']

	for i in cart:
		#We use try block to prevent items in cart that may have been removed from causing error
		try:
			cartItems += cart[i]['quantity']

			product = Product.objects.get(id=i)
			total = (product.price * cart[i]['quantity'])

			order['get_cart_total'] += total
			order['get_cart_items'] += cart[i]['quantity']

			item = {
				'id':product.id,
				'product':{'id':product.id,'name':product.name, 'price':product.price, 
				'main_image':product.main_image}, 'quantity':cart[i]['quantity'],
				'digital':product.digital,'get_total':total,
				}
			items.append(item)

			if product.digital == False:
				order['shipping'] = True
		except:
			pass
			
	return {'cartItems':cartItems ,'order':order, 'items':items}


# def wishlistData(request):

def cartData(request):
	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
		
	else:
		cookieData = cookieCart(request)
		cartItems = cookieData['cartItems']
		order = cookieData['order']
		items = cookieData['items']
		

	return {'cartItems':cartItems ,'order':order, 'items':items}


def wishlistData(request):
	if request.user.is_authenticated:
		customer = request.user
		
		wishlists = Wishlist.objects.filter(customer=request.user)
		wishlists_counts = Wishlist.objects.filter(customer=request.user).count()
	else:
		cookieWishlistData = cookieWishlist(request)

		wishlists = cookieWishlistData['wishlists']
		wishlists_counts = cookieWishlistData['wishlists_counts']

	return {'wishlists':wishlists,'wishlists_counts':wishlists_counts}



def guestOrder(request, data):
	name = data['form']['name']
	email = data['form']['email']

	cookieData = cookieCart(request)
	items = cookieData['items']

	customer, created = User.objects.get_or_create(
			email=email,
			)
	customer.name = name
	customer.save()

	order = Order.objects.create(
		customer=customer,
		complete=False,
		)

	for item in items:
		product = Product.objects.get(id=item['id'])
		orderItem = OrderItem.objects.create(
			product=product,
			order=order,
			quantity=item['quantity'],
		)
	return customer, order







