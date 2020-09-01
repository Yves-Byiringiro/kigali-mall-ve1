from django.urls import path
from .views import *





urlpatterns = [
    
    path('',homepage,name='homepage'),
	path('cart/', cart, name="cart"),
	path('wishlist/', wishlist, name="wishlist"),
	path('checkout/', checkout, name="checkout"),
	path('update_item/', updateItem, name="update_item"),
	path('process_order/', processOrder, name="process-order"),

	
	path('update_items/', updateItems, name="update_items"),
	path('destroy_wishlist/', destroy_wishlist, name="destroy_wishlist"),


	path('product_details/<slug>/', productDetails, name="product_details"),
	path('search_results/', productResults, name="products_results"),

	


	# new
	path('products/womens-fashions/', womensFashions, name="womensFashions"),
	path('products/mens-fashions/', mensFashions, name="mensFashions"),
	path('products/kids-fashions/', kidsFashions, name="kidsFashions"),
	path('products/cosmetics/', cosmetics, name="cosmetics"),
	path('products/accessories/', accessories, name="accessories"),


	path('shop/', shop, name="shop"),

]



