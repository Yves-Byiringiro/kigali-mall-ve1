from django.urls import path
from .views import *




urlpatterns = [
    path('products/',ProductList.as_view()),
    path('product-details/<int:pk>/',ProductDetails.as_view()),

    path('most-liked/',MostLiked.as_view()),
    path('most-liked/<int:pk>/',MostLikedDetails.as_view()),

    path('best-seller/',BestSeller.as_view()),
    path('best-seller/<int:pk>/',BestSellerDetails.as_view()),

    path('hot-trend/',HotTrend.as_view()),
    path('hot-trend/<int:pk>/',HotTrendDetails.as_view()),

    path('new-womens-products/',NewWomenProducts.as_view()),
    path('new-womens-products/<int:pk>/',NewWomenProductsDetails.as_view()),

    path('new-mens-products/',NewMenProducts.as_view()),
    path('new-mens-products/<int:pk>/',NewMenProductsDetails.as_view()),

    path('new-kids-products/',NewKidsProducts.as_view()),
    path('new-kids-products/<int:pk>/',NewKidsProductsDetails.as_view()),

    path('new-accessories-products/',NewAccessoriesProducts.as_view()),
    path('new-accessories-products/<int:pk>/',NewAccessoriesProductsDetails.as_view()),



    path('categories/',CategoryList.as_view()),

    
]
