from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.index, name='home'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('users/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register_user/', views.register_user, name='register_user'),
    path('users/<int:pk>/my-profile/', views.show_current_user_profile, name='my-profile'),
    path('users-sort-by-reg-date-desc/', views.sort_user_list_by_reg_date_desc, name='sort-users-by-reg-date-desc'),
    path('users-sort-by-username-asc/', views.sort_user_list_by_username_asc, name='sort-users-by-username-asc'),
    path('users-sort-by-username-desc', views.sort_user_list_by_username_desc, name='sort-users-by-username-desc'),

]