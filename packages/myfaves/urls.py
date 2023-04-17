from django.urls import path
from packages.myfaves import views

urlpatterns = [
    path('all/', views.show_my_favs_all, name='my-favs-all'),
    path('salads/', views.show_my_favs_salads, name='my-favs-salads'),
    path('first-course/', views.show_my_favs_first_course, name='my-favs-first-course'),
    path('main-course/', views.show_my_favs_main_course, name='my-favs-main-course'),
    path('dessert/', views.show_my_favs_dessert, name='my-favs-dessert'),
    path('bakery/', views.show_my_favs_bakery, name='my-favs-bakery'),
    path('beverages/', views.show_my_favs_beverages, name='my-favs-beverages'),
    ]