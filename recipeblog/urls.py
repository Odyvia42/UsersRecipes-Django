from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('users/', include('users.urls')),
    path('users/<int:pk>', views.show_user_profile, name='user-detail'),
    path('usersfavs/<int:pk>/', include('usersfavs.urls')),
    path('usersrecipes/<int:pk>/', include('usersrecipes.urls')),
    path('recipes/', include('recipes.urls')),
    path('recipes/<int:pk>', views.show_recipe_detail, name='recipe-detail'),
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
    path('myfaves/', include('packages.myfaves.urls')),
    path('myrecipes/', include('packages.myrecipes.urls')),
    path('tag/all-tags', views.show_all_tags, name='all-tags'),
    path('tag/<str:slug>', views.show_recipes_by_tag, name='show-recipes-by-tag'),
    path('users/all-authors', views.show_all_authors, name='all-authors'),
]
