from django.urls import path

from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('recipes/', views.RecipeListView.as_view()),
    path('recipes/<int:pk>/', views.RecipesDetailView.as_view()),
    path('recipes/<int:pk>/update/', views.RecipesDetailView.as_view()),
    path('recipes/<int:pk>/delete/', views.RecipesDetailView.as_view()),
    path('recipes/create/', views.RecipeCreateView.as_view()),
    path('user_list/', views.UserListView.as_view()),
    path('register/', views.UserCreateView.as_view()),
    path('login/', views.UserLoginView.as_view()),
    path('logout/', views.UserLogoutView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name = 'token_verify'),
]
