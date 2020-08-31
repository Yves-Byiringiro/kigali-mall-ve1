from django import forms
from .models import *




class ReviewForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Name'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'input','placeholder':'Email'}))
    review = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'input','placeholder':'Enter your username','rows':'5', 'cols':'47'}))

    class Meta:
        model = Review
        fields  = ('name','email','review',)




class ShippingAddressForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'state'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}))

    class Meta:
        model = ShippingAddress
        fields  = ('name','email','address','city','state','country','phone',)

