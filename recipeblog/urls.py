from django.urls import path, include
from . import views




urlpatterns=[
    path('', views.index, name='home'),

    path('users/', include('users.urls')),

    path('recipes/', include('recipes.urls')),




    path('recipes/<int:pk>', views.show_recipe_detail, name='recipe-detail'),
    path('users/<int:pk>', views.show_user_profile, name='user-detail'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('register_user/', views.register_user, name='register_user'),
    path('users/<int:pk>/my-profile/', views.show_current_user_profile, name='my-profile'),
    path('add-recipe', views.add_recipe, name='add-recipe'),
    path('recipes/update-recipe/<recipe_id>', views.update_recipe, name='update-recipe'),
    path('users/update-user/<user_id>', views.update_user, name='update-user'),
    path('password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('password-success/', views.change_password_success, name='password-success'),
    path('like/<int:pk>', views.like_recipe, name='like-recipe'),
    path('fave/<int:pk>', views.fave_recipe, name='fave-recipe'),

    path('myfaves/', include('myfaves.urls')),

    path('myrecipes/', include('myrecipes.urls')),

    path('users/<int:pk>/favs-all/', views.show_user_favs_all, name='user-favs-all'),
    path('users/<int:pk>/favs-salads/', views.show_user_favs_salads, name='user-favs-salads'),
    path('users/<int:pk>/favs-first-course/', views.show_user_favs_first_course, name='user-favs-first-course'),
    path('users/<int:pk>/favs-main-course/', views.show_user_favs_main_course, name='user-favs-main-course'),
    path('users/<int:pk>/favs-dessert/', views.show_user_favs_dessert, name='user-favs-dessert'),
    path('users/<int:pk>/favs-bakery/', views.show_user_favs_bakery, name='user-favs-bakery'),
    path('users/<int:pk>/favs-beverages/', views.show_user_favs_beverages, name='user-favs-beverages'),

    path('users/<int:pk>/recipes-all/', views.show_user_recipes_all, name='user-recipes-all'),
    path('users/<int:pk>/recipes-salads/', views.show_user_recipes_salads, name='user-recipes-salads'),
    path('users/<int:pk>/recipes-first-course/', views.show_user_recipes_first_course, name='user-recipes-first-course'),
    path('users/<int:pk>/recipes-main-course/', views.show_user_recipes_main_course, name='user-recipes-main-course'),
    path('users/<int:pk>/recipes-dessert/', views.show_user_recipes_dessert, name='user-recipes-dessert'),
    path('users/<int:pk>/recipes-bakery/', views.show_user_recipes_bakery, name='user-recipes-bakery'),
    path('users/<int:pk>/recipes-beverages/', views.show_user_recipes_beverages, name='user-recipes-beverages'),

    path('tag/all-tags', views.show_all_tags, name='all-tags'),
    path('tag/<str:slug>', views.show_recipes_by_tag, name='show-recipes-by-tag'),
    path('users/all-authors', views.show_all_authors, name='all-authors'),


]