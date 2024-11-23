from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/add/', views.recipe_add, name='recipe_add'),
    path('recipe/<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
]
