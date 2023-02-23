from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='home'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe-list'),

]