from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *



urlpatterns = [
    
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/change_password.html'), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
   

	path('account/', dashboard, name="dashboard"),
	path('cart/', userCart, name="user_cart"),
    path('finished_orders/', finished_orders, name="finished_orders"),
	path('wishlist/', userWishlist, name="user_wishlist"),
	path('change_password/', change_password, name="user_change_password"),
	path('update_profile/', update_profile, name="update_profile"),



]
