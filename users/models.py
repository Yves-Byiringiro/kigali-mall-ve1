from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone
from django_countries.fields import CountryField




class UserProfileManager(BaseUserManager):

    def create_user(self, email, name, gender, phone, city, country, password=None):
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, gender=gender, phone=phone, city=city, country=country)
        
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, name, gender, phone, city, country, password):

        user = self.create_user(email, name, gender, phone, city, country, password)
        
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user




class UserProfile(AbstractBaseUser, PermissionsMixin):
    GENDER = (
         ('Male','Male'),
        ('Female','Female'),
    )
    email = models.EmailField(unique=True, max_length=30)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER, default='Male')
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    country = CountryField(null=True , blank=True, blank_label='---------------------------------- choose your country ----------------------------------')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','gender','phone','city','country']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
        # return self.name.split()[1]