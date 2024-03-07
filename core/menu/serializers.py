from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Category, DishType, Ingredient, Recipe, IngredientsForRecipe


class RecipeListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = ('id', 'user', 'category', 'created_date', 'updated_date')


class RecipeDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = ('title', 'description')

class RecipeCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = ('user', 'title', 'description', 'category', 'dish_type', 'ingredient', 'cooking_time')