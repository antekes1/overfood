from django.shortcuts import render,redirect
from .models import Recipe, Products
from .forms import SearchForm, AddRecipe, AddProduct

# Create your views here.

def home(request):

    context = {}
    return render(request, 'home.html', context)

def eat_page(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            selected_products = form.cleaned_data['products']
            # recipes = Recipe.objects.filter(products__in=selected_products).distinct()
            recipes = Recipe.objects.all()
            matching_recipes = []

            for recipe in recipes:
                recipe_products = recipe.products.all()
                if set(recipe_products).issubset(selected_products):
                    if recipe.verify == 'True':
                        matching_recipes.append(recipe)
            print(matching_recipes)

        else:
            print("Hej masz coś zjebane")
            matching_recipes = []
    else:
        form = SearchForm()
        matching_recipes = []

    context = {'form':form, 'recipes': matching_recipes}
    return render(request, 'eat_page.html', context)

def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)

    context = {'recipe':recipe}
    return render(request, 'recipe.html', context)

def create_recipe(request):
    form = AddRecipe()

    if request.method == 'POST':
        form = AddRecipe(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('eat_page')
        else:
            print('Zejb')

    context = {'form': form}
    return render(request, 'recipe_form.html', context)

def create_product(request):
    form = AddProduct()

    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('create-recipe')
        else:
            print('Zejb')

    context = {'form': form}
    return render(request, 'product_form.html', context)
