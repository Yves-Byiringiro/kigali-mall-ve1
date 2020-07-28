from django import forms
from .models import *




class ReviewForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Name'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'input','placeholder':'Email'}))
    review = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'input', 'placeholder':'Review goes here','rows':'5', 'cols':'100'}))

    class Meta:
        model = Review
        fields  = ('name','email','review',)



class MomoTranctionIDForm(forms.ModelForm):
    transaction_id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter mobile money transaction id','label':''}))

    class Meta:
        model = MomoTranctionID
        fields = ('transaction_id',)