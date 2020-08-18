from django.contrib import admin
from .models import *




class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message','submitted_date']
    list_filter = ['submitted_date','name']


admin.site.register(Contact,ContactAdmin)
