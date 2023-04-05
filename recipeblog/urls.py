from django.urls import path, include
from . import views




urlpatterns=[
    path('', views.index, name='home'),
    path('users-sort-by-reg-date-asc/', views.sort_user_list_by_reg_date_asc, name='sort-users-by-reg-date-asc'),
    path('users-sort-by-reg-date-desc/', views.sort_user_list_by_reg_date_desc, name='sort-users-by-reg-date-desc'),
    path('users-sort-by-username-asc/', views.sort_user_list_by_username_asc, name='sort-users-by-username-asc'),
    path('users-sort-by-username-desc', views.sort_user_list_by_username_desc, name='sort-users-by-username-desc'),
    path('users-sort-by-recipes-amount-asc/', views.sort_user_list_by_recipes_amount_asc,
         name='sort-users-by-recipes-amount-asc'),
    path('users-sort-by-recipes-amount-desc/', views.sort_user_list_by_recipes_amount_desc,
         name='sort-users-by-recipes-amount-desc'),
    path('users-sort-by-rating-asc/', views.sort_user_list_by_rating_asc,
         name='sort-users-by-rating-asc'),
    path('users-sort-by-rating-desc/', views.sort_user_list_by_rating_desc,
         name='sort-users-by-rating-desc'),


    path('all-recipes-sort-by-pub-date-desc/', views.sort_all_recipes_by_pub_date_desc,
         name='sort-all-recipes-by-pub-date-desc'),
    path('all-recipes-sort-by-pub-date-asc/', views.sort_all_recipes_by_pub_date_asc,
         name='sort-all-recipes-by-pub-date-asc'),
    path('all-recipes-sort-by-title-desc/', views.sort_all_recipes_by_title_desc,
         name='sort-all-recipes-by-title-desc'),
    path('all-recipes-sort-by-title-asc/', views.sort_all_recipes_by_title_asc,
         name='sort-all-recipes-by-title-asc'),
    path('all-recipes-sort-by-likes-desc/', views.sort_all_recipes_by_likes_desc,
         name='sort-all-recipes-by-likes-desc'),
    path('all-recipes-sort-by-likes-asc/', views.sort_all_recipes_by_likes_asc,
         name='sort-all-recipes-by-likes-asc'),

    path('salads-sort-by-pub-date-desc/', views.sort_salads_by_pub_date_desc,
         name='sort-salads-by-pub-date-desc'),
    path('salads-sort-by-pub-date-asc/', views.sort_salads_by_pub_date_asc,
         name='sort-salads-by-pub-date-asc'),
    path('salads-sort-by-title-desc/', views.sort_salads_by_title_desc,
         name='sort-salads-by-title-desc'),
    path('salads-sort-by-title-asc/', views.sort_salads_by_title_asc,
         name='sort-salads-by-title-asc'),
    path('salads-sort-by-likes-desc/', views.sort_salads_by_likes_desc,
         name='sort-salads-by-likes-desc'),
    path('salads-sort-by-likes-asc/', views.sort_salads_by_likes_asc,
         name='sort-salads-by-likes-asc'),

    path('first-courses-sort-by-pub-date-desc/', views.sort_first_courses_by_pub_date_desc,
         name='sort-first-courses-by-pub-date-desc'),
    path('first-courses-sort-by-pub-date-asc/', views.sort_first_courses_by_pub_date_asc,
         name='sort-first-courses-by-pub-date-asc'),
    path('first-courses-sort-by-title-desc/', views.sort_first_courses_by_title_desc,
         name='sort-first-courses-by-title-desc'),
    path('first-courses-sort-by-title-asc/', views.sort_first_courses_by_title_asc,
         name='sort-first-courses-by-title-asc'),
    path('first-courses-sort-by-likes-desc/', views.sort_first_courses_by_likes_desc,
         name='sort-first-courses-by-likes-desc'),
    path('first-courses-sort-by-likes-asc/', views.sort_first_courses_by_likes_asc,
         name='sort-first-courses-by-likes-asc'),

    path('main-courses-sort-by-pub-date-desc/', views.sort_main_courses_by_pub_date_desc,
         name='sort-main-courses-by-pub-date-desc'),
    path('main-courses-sort-by-pub-date-asc/', views.sort_main_courses_by_pub_date_asc,
         name='sort-main-courses-by-pub-date-asc'),
    path('main-courses-sort-by-title-desc/', views.sort_main_courses_by_title_desc,
         name='sort-main-courses-by-title-desc'),
    path('main-courses-sort-by-title-asc/', views.sort_main_courses_by_title_asc,
         name='sort-main-courses-by-title-asc'),
    path('main-courses-sort-by-likes-desc/', views.sort_main_courses_by_likes_desc,
         name='sort-main-courses-by-likes-desc'),
    path('main-courses-sort-by-likes-asc/', views.sort_main_courses_by_likes_asc,
         name='sort-main-courses-by-likes-asc'),

    path('bakery-sort-by-pub-date-desc/', views.sort_bakery_by_pub_date_desc,
         name='sort-bakery-by-pub-date-desc'),
    path('bakery-sort-by-pub-date-asc/', views.sort_bakery_by_pub_date_asc,
         name='sort-bakery-by-pub-date-asc'),
    path('bakery-sort-by-title-desc/', views.sort_bakery_by_title_desc,
         name='sort-bakery-by-title-desc'),
    path('bakery-sort-by-title-asc/', views.sort_bakery_by_title_asc,
         name='sort-bakery-by-title-asc'),
    path('bakery-sort-by-likes-desc/', views.sort_bakery_by_likes_desc,
         name='sort-bakery-by-likes-desc'),
    path('bakery-sort-by-likes-asc/', views.sort_bakery_by_likes_asc,
         name='sort-bakery-by-likes-asc'),

    path('desserts-sort-by-pub-date-desc/', views.sort_desserts_by_pub_date_desc,
         name='sort-desserts-by-pub-date-desc'),
    path('desserts-sort-by-pub-date-asc/', views.sort_desserts_by_pub_date_asc,
         name='sort-desserts-by-pub-date-asc'),
    path('desserts-sort-by-title-desc/', views.sort_desserts_by_title_desc,
         name='sort-desserts-by-title-desc'),
    path('desserts-sort-by-title-asc/', views.sort_desserts_by_title_asc,
         name='sort-desserts-by-title-asc'),
    path('desserts-sort-by-likes-desc/', views.sort_desserts_by_likes_desc,
         name='sort-desserts-by-likes-desc'),
    path('desserts-sort-by-likes-asc/', views.sort_desserts_by_likes_asc,
         name='sort-desserts-by-likes-asc'),

    path('beverages-sort-by-pub-date-desc/', views.sort_beverages_by_pub_date_desc,
         name='sort-beverages-by-pub-date-desc'),
    path('beverages-sort-by-pub-date-asc/', views.sort_beverages_by_pub_date_asc,
         name='sort-beverages-by-pub-date-asc'),
    path('beverages-sort-by-title-desc/', views.sort_beverages_by_title_desc,
         name='sort-beverages-by-title-desc'),
    path('beverages-sort-by-title-asc/', views.sort_beverages_by_title_asc,
         name='sort-beverages-by-title-asc'),
    path('beverages-sort-by-likes-desc/', views.sort_beverages_by_likes_desc,
         name='sort-beverages-by-likes-desc'),
    path('beverages-sort-by-likes-asc/', views.sort_beverages_by_likes_asc,
         name='sort-beverages-by-likes-asc'),

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

    path('my-favs-all', views.show_my_favs_all, name='my-favs-all'),
    path('my-favs-salads', views.show_my_favs_salads, name='my-favs-salads'),
    path('my-favs-first-course', views.show_my_favs_first_course, name='my-favs-first-course'),
    path('my-favs-main-course', views.show_my_favs_main_course, name='my-favs-main-course'),
    path('my-favs-dessert', views.show_my_favs_dessert, name='my-favs-dessert'),
    path('my-favs-bakery', views.show_my_favs_bakery, name='my-favs-bakery'),
    path('my-favs-beverages', views.show_my_favs_beverages, name='my-favs-beverages'),

    path('my-recipes-all', views.show_my_recipes_all, name='my-recipes-all'),
    path('my-recipes-salads', views.show_my_recipes_salads, name='my-recipes-salads'),
    path('my-recipes-first-course', views.show_my_recipes_first_course, name='my-recipes-first-course'),
    path('my-recipes-main-course', views.show_my_recipes_main_course, name='my-recipes-main-course'),
    path('my-recipes-dessert', views.show_my_recipes_dessert, name='my-recipes-dessert'),
    path('my-recipes-bakery', views.show_my_recipes_bakery, name='my-recipes-bakery'),
    path('my-recipes-beverages', views.show_my_recipes_beverages, name='my-recipes-beverages'),

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

]