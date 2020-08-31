from django.contrib import admin
from .models import *



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','delivery_minutes','seller','date_added']
    list_filter = ['category','seller','date_added','delivery_minutes']
    list_per_page = 10



class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name','email','review','product','published','date_added']
    list_filter = ['product','date_added','name','published']
    list_per_page = 10


class WishlistAdmin(admin.ModelAdmin):
    list_display = ['customer','product','date_added']
    list_filter = ['customer','product','date_added']
    list_per_page = 10



class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','complete','transaction_id','date_ordered']
    list_filter = ['customer','date_ordered','complete']
    list_per_page = 10



class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product','order','quantity','date_added']
    list_filter = ['product','date_added']
    list_per_page = 10




class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['customer','order','address','city','state','country','phone','date_added']
    list_filter = ['customer','city','state','date_added']
    list_per_page = 10






class SellerDAdmin(admin.ModelAdmin):
    list_display = ['name','phone','date_added']
    list_filter = ['date_added']
    list_per_page = 10



admin.site.register(Category)
admin.site.register(Seller,SellerDAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(ProductImage)
admin.site.register(Wishlist,WishlistAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(ShippingAddress,ShippingAddressAdmin)
admin.site.register(Mymomo)


