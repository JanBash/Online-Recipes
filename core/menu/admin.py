from django.contrib import admin

from .models import Category, DishType, Ingredient, Recipe, IngredientsForRecipe

admin.site.register(Category)
admin.site.register(DishType)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(IngredientsForRecipe)
