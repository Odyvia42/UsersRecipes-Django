from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='home'),
    path('user-list/', views.UserListView.as_view()),
    path('recipe-list/', views.RecipeListView.as_view()),
]