from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('eat', views.eat_page, name='eat_page'),
    path('create-recipe', views.create_recipe, name='create-recipe'),
    path('create-product', views.create_product, name='create-product'),
    path('recipe/<str:pk>/', views.recipe, name="recipe"),
]