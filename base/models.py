from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    preparation = models.TextField(null=True)
    time = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)  # DecimalField z dwoma miejscami po przecinku
    products = models.ManyToManyField(Products, related_name='products')
    calories = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    portions_count = models.CharField(max_length=200, blank=True, null=True)
    ingredients_count = models.TextField(null=True)
    verify = models.CharField(max_length=50, default="False")


    def __str__(self):
        return self.name

