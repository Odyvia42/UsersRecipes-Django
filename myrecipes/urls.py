from django.urls import path
from recipeblog import views

urlpatterns = [
    path('all/', views.show_my_recipes_all, name='my-recipes-all'),
    path('salads/', views.show_my_recipes_salads, name='my-recipes-salads'),
    path('first-course/', views.show_my_recipes_first_course, name='my-recipes-first-course'),
    path('main-course/', views.show_my_recipes_main_course, name='my-recipes-main-course'),
    path('dessert/', views.show_my_recipes_dessert, name='my-recipes-dessert'),
    path('bakery/', views.show_my_recipes_bakery, name='my-recipes-bakery'),
    path('beverages/', views.show_my_recipes_beverages, name='my-recipes-beverages'),
    ]