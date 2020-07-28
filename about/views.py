from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm
from store.utils import  cartData, wishlistData
from store.models import *



def about(request):
    data = cartData(request)
    data2 = wishlistData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    wishlists_counts = data2['wishlists_counts']

    categories = Category.objects.all()



    context = {
        'cartItems':cartItems,
        'order':order,
        'items':items,
        'categories':categories,
        'wishlists_counts':wishlists_counts

    }

    return render(request, 'about/about.html',context)


def contact_us(request):
    data = cartData(request)
    data2 = wishlistData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    wishlists_counts = data2['wishlists_counts']
    
    categories = Category.objects.all()



    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('contact_us')
    else:
        form = ContactForm()

    context = {
        'cartItems':cartItems,
        'order':order,
        'items':items,
        'categories':categories,
        'form':form,
        'wishlists_counts':wishlists_counts
    }
    return render(request, 'about/contact_us.html', context)



def help(request):
    data = cartData(request)
    data2 = wishlistData(request)
    
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    wishlists_counts = data2['wishlists_counts']

    categories = Category.objects.all()


    context = {
        'cartItems':cartItems,
        'order':order,
        'items':items,
        'categories':categories,
        'wishlists_counts':wishlists_counts
    }
    return render(request, 'about/help.html',context)


def privacy_policy(request):
    data = cartData(request)
    data2 = wishlistData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    wishlists_counts = data2['wishlists_counts']

    categories = Category.objects.all()



    context = {
        'cartItems':cartItems,
        'order':order,
        'items':items,
        'categories':categories,
        'wishlists_counts':wishlists_counts
    }
    return render(request, 'about/privacy_policy.html',context)


def terms_conditions(request):
    data = cartData(request)
    data2 = wishlistData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    wishlists_counts = data2['wishlists_counts']

    categories = Category.objects.all()



    context = {
        'cartItems':cartItems,
        'order':order,
        'items':items,
        'categories':categories,
        'wishlists_counts':wishlists_counts
    }
    return render(request, 'about/terms_conditions.html',context)