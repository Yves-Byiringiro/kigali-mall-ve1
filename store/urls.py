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
	path('results/', productResults, name="products_results"),

	
	path('products/laptops/', laptops, name="laptops"),
	path('products/smartphones/', smartphones, name="smartphones"),
	path('products/cameras/', cameras, name="cameras"),
	path('products/accessories/', accessories, name="accessories"),
	path('products/shoes/', shoes, name="shoes"),
	path('products/home-furnitures/', home_furnitures, name="home_furnitures"),



]



