from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.index, name='home'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('users/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('accounts/', include('django.contrib.auth.urls'))
]