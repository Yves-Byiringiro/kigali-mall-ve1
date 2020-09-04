from django.db import models
from django.contrib.auth.models import User
from kigalimall.settings import AUTH_USER_MODEL
from store.slugs import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from django.core.exceptions import ValidationError

User = settings.AUTH_USER_MODEL






class Seller(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True)
    phone  = models.CharField(max_length=15,default='078 000 0000')
    date_added  = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'




class Product(models.Model):
    COLOR = (
        ('Black', 'Black'), 
        ('Red', 'Red'), 
        ('White', 'White'),
        ('Silver', 'Silver'),
        ('Gray', 'Gray'),
        ('Yellow', 'Yellow'),
        ('Pink', 'Pink'),
        ('Dark blue', 'Dark blue'),
        ('Light blue', 'Light blue'),
        ('Black and white', 'Black and white'),
        ('Gold', 'Gold'),
        ('Not Specified', 'Not Specified'),




        )

    SUB_CATEGORIES = (
        ('Shoes', 'Shoes'), 
        ('Sutes', 'Sutes'),
        ('Clothes', 'Clothes'),
        ('Shirts', 'Shirts'),
        ('TShirts', 'TShirts'),
        ('Jeans', 'Jeans'),
        ('Phones', 'Phones'),
        ('Laptops', 'Laptops')




        )

    name = models.CharField(max_length=250,unique=True)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null=True, blank=True,related_name='products')
    sub_category = models.CharField(max_length=200,choices=SUB_CATEGORIES, default='Shoes', blank=True, null=True)
    price = models.DecimalField( max_digits=10, decimal_places=1)
    price_dollar = models.DecimalField( max_digits=7, decimal_places=2, default=1, null=True, blank=True)
    digital = models.BooleanField(default=False,null=True,blank=True)
    main_image = models.ImageField(upload_to='products')
    color = models.CharField(max_length=200,choices=COLOR, default='Black', blank=True, null=True)
    size = models.CharField(max_length=50,null=True, blank=True,default='not specified')
    delivery_minutes = models.CharField(max_length=50, default='2 hours')
    in_stock = models.BooleanField(default=False,null=True,blank=True)
    description = models.TextField(blank=True)
    slug  = models.SlugField(blank=True, null=True, max_length=250)
    filter = models.CharField(max_length=50, help_text='Enter: men , women , kid , accessories , cosmetic', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def old_price(self):
        old_price = self.price + 1500
        return old_price

    def rate(self):
        rate = self.price / self.price_dollar
        return rate

    class Meta:
        ordering = ["-date_added"]

    def get_absolute_url(self):
        return reverse('product_details', kwargs={'slug':self.slug})

def pre_save_receiver(sender, instance, *args, **kwargs): 
   if not instance.slug: 
       instance.slug = unique_slug_generator(instance) 
  
pre_save.connect(pre_save_receiver, sender = Product) 


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, related_name='product_images')
    image = models.ImageField(upload_to='products', null=True, blank=True)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=250)
    email = models.EmailField()
    review = models.CharField(max_length=800)
    published = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    

class Wishlist(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)


    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping



    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        # total = sub_total + self.shipping_price
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,blank=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    country = models.CharField(max_length=200, null=False)
    phone = models.CharField(max_length=12, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Shipping Address'
        verbose_name_plural = 'Shipping Addresses'

    def __str__(self):
        return self.address
    


    

class Mymomo(models.Model):
    name = models.CharField(max_length=30, default="Yves Byiringiro")
    number = models.CharField(max_length=13, default="0781 433 445")


    def __str__(self):
        return self.name

