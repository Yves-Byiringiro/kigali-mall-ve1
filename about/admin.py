from django.contrib import admin
from .models import *



class ActiveCarouselAdmin(admin.ModelAdmin):
    list_display = ['header','image','content','animation']


class CarouselAdmin(admin.ModelAdmin):
    list_display = ['header','image','content','animation']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message','submitted_date']
    list_filter = ['submitted_date','name']



admin.site.register(ActiveCarousel,ActiveCarouselAdmin)
admin.site.register(Carousel,CarouselAdmin)
admin.site.register(Contact,ContactAdmin)
