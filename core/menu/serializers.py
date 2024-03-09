from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Category, DishType, Ingredient, Recipe, IngredientsForRecipe


class RecipeListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = ('id', 'user', 'category', 'created_date', 'updated_date')

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('title', )

class DishTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DishType
        fields = ('title', )

class IngredientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ingredient
        fields = '__all__'

class IngredientsForRecipeSerializer(serializers.ModelSerializer):
    
    ingredient = IngredientSerializer()
    
    class Meta:
        model = IngredientsForRecipe
        fields = '__all__'

class RecipeDetailSerializer(serializers.ModelSerializer):
    
    ingredient = IngredientsForRecipeSerializer()
    category = serializers.CharField(source = 'category.title')
    dish_type = serializers.CharField(source = 'dish_type.title')
    
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'ingredient', 'cooking_time', 'category', 'dish_type')

class RecipeUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = ('title', 'description')

class RecipeCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = ('user', 'title', 'description', 'category', 'dish_type', 'ingredient', 'cooking_time')

class UserListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class UserRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        
        return user
    
    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            if field == 'password':
                instance.set_password(value)
            else:
                setattr(instance, field, value)
        instance.save()
        return instance

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style = {'input_type': 'password'},
        trim_whitespace = False,
        write_only = True
    )
    
    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')
        
        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request = self.context.get('requet'),
                                username = username, password = password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code = 'authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code = 'authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs