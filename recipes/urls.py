from django.urls import path
from .views import index, AddProductRecipeView, CookRecipeView, show_recipes

urlpatterns = [
    path('', index),
    path('add_product_to_recipe', AddProductRecipeView.as_view()),
    path('cook_recipe', CookRecipeView.as_view()),
    path('show_recipes_without_product/<int:product_id>/', show_recipes),
]
