from django import forms
from django.forms import ModelForm
from .models import Recipe, Products


class SearchForm(forms.Form):
    products = forms.ModelMultipleChoiceField(
        queryset=Products.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'products-checkbox'}),
    )

class AddRecipe(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'preparation', 'time', 'products', 'calories', 'portions_count', 'ingredients_count']
        # dodać password

class AddProduct(ModelForm):
    class Meta:
        model = Products
        fields = ['name']
