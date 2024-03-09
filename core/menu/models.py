from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)

class DishType(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)

class Ingredient(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)

class Recipe(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    ingredient = models.ForeignKey('IngredientsForRecipe', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    cooking_time = models.DurationField()
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    dish_type = models.ForeignKey(DishType, on_delete = models.PROTECT)
    created_date = models.DateField(auto_now_add = True)
    updated_date = models.DateField(auto_now_add = True)

class IngredientsForRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    unit_of_measure = models.CharField(max_length = 50)     