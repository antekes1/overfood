from django.contrib import admin

from .models import Recipe, Products

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Products)