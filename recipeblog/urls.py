from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='home'),
    path('user-list/', views.UserListView.as_view(), name='user-list'),
    path('recipe_list/', views.RecipeListView.as_view(), name='recipe-list'),
]