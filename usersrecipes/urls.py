from django.urls import path

from recipeblog import views

urlpatterns = [
    path('all/', views.show_user_recipes_all, name='user-recipes-all'),
    path('salads/', views.show_user_recipes_salads, name='user-recipes-salads'),
    path('first-course/', views.show_user_recipes_first_course, name='user-recipes-first-course'),
    path('main-course/', views.show_user_recipes_main_course, name='user-recipes-main-course'),
    path('dessert/', views.show_user_recipes_dessert, name='user-recipes-dessert'),
    path('bakery/', views.show_user_recipes_bakery, name='user-recipes-bakery'),
    path('beverages/', views.show_user_recipes_beverages, name='user-recipes-beverages'),
    ]