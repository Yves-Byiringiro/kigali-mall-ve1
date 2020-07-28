from django import forms
from .models import *



class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Subject'}))
    message = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message goes here','rows':'5', 'cols':'100'}))
    class Meta:
        model = Contact
        fields  = ('name','email','subject','message',)