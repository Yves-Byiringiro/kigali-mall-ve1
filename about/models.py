from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=160, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=500)
    submitted_date = models.DateTimeField(auto_now_add=True)