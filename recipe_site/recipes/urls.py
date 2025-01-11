from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('add/', views.add_recipe, name='add_recipe'),
]