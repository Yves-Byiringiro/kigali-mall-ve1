from django.db import models


class ActiveCarousel(models.Model):
    header = models.CharField(max_length=600)
    content = models.TextField()
    image = models.ImageField(upload_to='carousels')
    animation = models.CharField(max_length=200, blank=True,help_text="Enter: fadeInDown    zoomInLeft  zoomInRight")

class Carousel(models.Model):
    header = models.CharField(max_length=600)
    content = models.TextField()
    image = models.ImageField(upload_to='carousels')
    animation = models.CharField(max_length=200, blank=True,help_text="Enter: fadeInDown   zoomInLeft   zoomInRight")

class Contact(models.Model):
    name = models.CharField(max_length=160, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=500)
    submitted_date = models.DateTimeField(auto_now_add=True)