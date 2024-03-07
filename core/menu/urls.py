from django.urls import path

from . import views

urlpatterns = [
    path('recipes/', views.RecipeListView.as_view()),
    path('recipes/<int:pk>', views.RecipesDetailView.as_view()),
    path('recipes/<int:pk>/update/', views.RecipesDetailView.as_view()),
    path('recipes/<int:pk>/delete/', views.RecipesDetailView.as_view()),
    path('recipes/create/', views.RecipeCreateView.as_view()),
]
