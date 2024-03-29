from django import forms
from .models import *




class ReviewForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Name'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'input','placeholder':'Email'}))
    review = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'input','placeholder':'Enter your username','rows':'5', 'cols':'47'}))

    class Meta:
        model = Review
        fields  = ('name','email','review',)

