from rest_framework import serializers
from store.models import Product, Category






class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source = 'category.name')
    class Meta:
        model = Product
        fields = ['id','name','category','sub_category','price','main_image','color','size','delivery_minutes','in_stock','description']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']