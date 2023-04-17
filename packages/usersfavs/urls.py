from django.urls import path

from packages.usersfavs import views

urlpatterns = [
    path('favs-all/', views.show_user_favs_all, name='user-favs-all'),
    path('favs-salads/', views.show_user_favs_salads, name='user-favs-salads'),
    path('favs-first-course/', views.show_user_favs_first_course, name='user-favs-first-course'),
    path('favs-main-course/', views.show_user_favs_main_course, name='user-favs-main-course'),
    path('favs-dessert/', views.show_user_favs_dessert, name='user-favs-dessert'),
    path('favs-bakery/', views.show_user_favs_bakery, name='user-favs-bakery'),
    path('favs-beverages/', views.show_user_favs_beverages, name='user-favs-beverages'),
    ]