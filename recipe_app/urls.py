from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeList.as_view(), name='recipe_list'),
    path('recipe-create', views.RecipeCreate.as_view(), name='recipe_create'),
    path('recipe-detail/<int:pk>', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('recipe-update/<int:pk>', views.RecipeUpdate.as_view(), name='recipe_update'),
    path('recipe-delete/<int:pk>', views.RecipeDelete.as_view(), name='recipe_delete'),
]