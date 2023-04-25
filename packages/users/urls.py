from django.urls import path
from packages.users import views

urlpatterns = [
    path('sort-by-reg-date-asc/', views.sort_user_list_by_reg_date_asc, name='sort-users-by-reg-date-asc'),
    path('sort-by-reg-date-desc/', views.sort_user_list_by_reg_date_desc, name='sort-users-by-reg-date-desc'),
    path('sort-by-username-asc/', views.sort_user_list_by_username_asc, name='sort-users-by-username-asc'),
    path('sort-by-username-desc/', views.sort_user_list_by_username_desc, name='sort-users-by-username-desc'),
    path('sort-by-recipes-amount-asc/', views.sort_user_list_by_recipes_amount_asc,
         name='sort-users-by-recipes-amount-asc'),
    path('sort-by-recipes-amount-desc/', views.sort_user_list_by_recipes_amount_desc,
         name='sort-users-by-recipes-amount-desc'),
    path('sort-by-rating-asc/', views.sort_user_list_by_rating_asc,
         name='sort-users-by-rating-asc'),
    path('sort-by-rating-desc/', views.sort_user_list_by_rating_desc,
         name='sort-users-by-rating-desc'),
]
