from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.db import models
from .models import RecipeProduct, Product, Recipe


def index(request):
    return HttpResponse("Hello, Chef!")


class AddProductRecipeView(View):
    def get(self, request, *args, **kwargs):
        try:
            # Getting Parameters from GET Request
            weight = request.GET.get('weight')
            recipe = Recipe.objects.get(pk=request.GET.get('recipe_id'))
            product = Product.objects.get(pk=request.GET.get('product_id'))

            if not RecipeProduct.objects.filter(recipe_id=recipe, product_id=product):
                RecipeProduct.objects.create(
                    recipe_id=recipe,
                    product_id=product,
                    weight=int(weight)
                )
            else:
                RecipeProduct.objects.filter(
                    recipe_id=recipe,
                    product_id=product
                ).update(
                    weight=int(weight)
                )
        except:
            return HttpResponse("Parameters are wrong!")

        return HttpResponse(f"{recipe.name}<br>{product.name} - {weight}g")


class CookRecipeView(View):
    def get(self, request, *args, **kwargs):
        try:
            products = Product.objects.filter(recipeproduct__recipe_id=request.GET.get('recipe_id'))
        except:
            return HttpResponse("Parameter is wrong")

        if products:
            products.update(prep_count=models.F('prep_count')+1)
            return HttpResponse("Updated")

        return HttpResponse("Recipe Not Found")


def show_recipes(request, product_id):
    recipes = ([r for r in Recipe.objects.exclude(recipeproduct__product_id=product_id)]
               + [r for r in Recipe.objects.filter(recipeproduct__product_id=product_id, recipeproduct__weight__lt=10)])

    context = {'recipes': recipes, 'product_id': product_id}
    return render(request, 'recipes_table.html', context)
