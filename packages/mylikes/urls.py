from django.urls import path
from packages.mylikes import views

urlpatterns = [
    path('all/', views.show_my_likes_all, name='my-likes-all'),
    path('salads/', views.show_my_likes_salads, name='my-likes-salads'),
    path('first-course/', views.show_my_likes_first_course, name='my-likes-first-course'),
    path('main-course/', views.show_my_likes_main_course, name='my-likes-main-course'),
    path('dessert/', views.show_my_likes_dessert, name='my-likes-dessert'),
    path('bakery/', views.show_my_likes_bakery, name='my-likes-bakery'),
    path('beverages/', views.show_my_likes_beverages, name='my-likes-beverages'),
    ]