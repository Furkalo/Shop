from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from shop.models import Product

class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)  # User's email (unique)
    full_name = models.CharField(max_length=100)  # User's full name
    is_admin = models.BooleanField(default=False)  # Admin status
    is_active = models.BooleanField(default=True)  # Active status
    likes = models.ManyToManyField(Product, blank=True, related_name='likes')  # Products liked by the user
    is_manager = models.BooleanField(default=False)  # Manager role flag

    objects = UserManager()  # Custom user manager

    USERNAME_FIELD = 'email'  # Email as the unique identifier
    REQUIRED_FIELDS = ['full_name']  # Fields required when creating a user

    def __str__(self):
        return self.email  # Return email as the string representation

    def has_perm(self, perm, obj=None):
        return True  # User has all permissions

    def has_module_perms(self, app_label):
        return True  # User has permissions for the app

    @property
    def is_staff(self):
        return self.is_admin  # User is staff if they are admin

    def get_likes_count(self):
        return self.likes.count()  # Returns the number of liked products
