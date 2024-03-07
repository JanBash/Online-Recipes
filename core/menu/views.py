from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated

from .models import Recipe
from .serializers import RecipeListSerializer, RecipeDetailSerializer, RecipeUpdateSerializer, RecipeCreateSerializer


class RecipeListView(APIView):
    
    def get(self, request):
        
        recipes = Recipe.objects.all()
        
        serializer = RecipeListSerializer(recipes, many = True)
        
        return Response(serializer.data)


class RecipesDetailView(APIView):
    
    def get(self, request, pk):
        
        recipe = Recipe.objects.filter(id = pk).first()
        
        serializer = RecipeDetailSerializer(recipe)
        
        return Response(serializer.data)
    
    def patch(self, request, pk):
        
        recipe = get_object_or_404(Recipe.objects.all(), id = pk)
        
        serializer = RecipeUpdateSerializer(recipe, data = request.data)
        
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            
            return Response(status = status.HTTP_200_OK)
        
        return Response(status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
         recipe = get_object_or_404(Recipe.objects.all(), id = pk)
         
         recipe.delete()
         
         return Response(status = status.HTTP_204_NO_CONTENT)

class RecipeCreateView(APIView):
    
    
    def post(self, request):
        
        serializer = RecipeCreateSerializer(data = request.data, context = {'request': request})
        
        if serializer.is_valid(raise_exception = True):
            serializer.save()

            return Response(status = status.HTTP_201_CREATED)
        
        return Response(status = status.HTTP_400_BAD_REQUEST)