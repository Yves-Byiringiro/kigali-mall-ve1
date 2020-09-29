from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

from .models import UserProfile
from .forms import *

from store.utils import  cartData
from store.models import *
from about.models import *


class RegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm
    
    # def form_valid(self, form):

    #     return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)
        messages.success(self.request, 'Your account has been created successfully !.')
        return success_url




@login_required
def dashboard(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    categories = Category.objects.all()
    
    wishlists_counts = Wishlist.objects.filter(customer=request.user).count()


    context = {
        'cartItems':cartItems,
        'order':order,
        'items':items,
        'categories':categories,
        'wishlists_counts':wishlists_counts
    }

    
    return render(request, 'users/dashboard.html',context)


@login_required
def userCart(request):

    data = cartData(request)
    
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    categories = Category.objects.all()

    wishlists_counts = Wishlist.objects.filter(customer=request.user).count()

    
    context = {
        'items':items, 
        'order':order, 
        'cartItems':cartItems,
        'categories':categories,
        'wishlists_counts':wishlists_counts
        }
    return render(request, 'users/userCart.html', context)


@login_required
def finished_orders(request):
    finished_orders = MomoTranctionID.objects.filter(confirmed=False)
    template_name = 'users/finished_orders.html'
    context = {'finished_orders': finished_orders}
    return render(request, template_name, context)

@login_required
def userWishlist(request):
    data = cartData(request)
    
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    categories = Category.objects.all()

    wishlists = Wishlist.objects.filter(customer=request.user)
    wishlists_counts = Wishlist.objects.filter(customer=request.user).count()

    
    context = {
        'items':items, 
        'order':order, 
        'cartItems':cartItems,
        'categories':categories,
        'wishlists':wishlists,
        'wishlists_counts':wishlists_counts
        }

    return render(request, 'users/userWishlist.html', context)



@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password has been changed successfully !.')
            return redirect('dashboard')
        else:
            return redirect('user_change_password')
    else:
        form = PasswordChangeForm(user=request.user)

    data = cartData(request)
    
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    categories = Category.objects.all()
    wishlists_counts = Wishlist.objects.filter(customer=request.user).count()

    context = {
        'items':items, 
        'order':order, 
        'cartItems':cartItems,
        'categories':categories,
        'form': form,
        'wishlists_counts':wishlists_counts
        }
    return render(request, 'users/change_password.html',context)





@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileUpdateForm(instance=request.user)
    
    data = cartData(request)
    
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    categories = Category.objects.all()

    wishlists_counts = Wishlist.objects.filter(customer=request.user).count()
    
    context = {
        'items':items, 
        'order':order, 
        'cartItems':cartItems,
        'categories':categories,
        'form':form,
        'wishlists_counts':wishlists_counts

    }
    return render(request, 'users/update_profile.html', context)































