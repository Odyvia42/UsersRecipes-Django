from django.urls import path, include
from packages.recipes import views

all_recipes_patterns = [
    path('sort-by-pub-date-desc/', views.sort_all_recipes_by_pub_date_desc,
         name='sort-all-recipes-by-pub-date-desc'),
    path('sort-by-pub-date-asc/', views.sort_all_recipes_by_pub_date_asc,
         name='sort-all-recipes-by-pub-date-asc'),
    path('sort-by-title-desc/', views.sort_all_recipes_by_title_desc,
         name='sort-all-recipes-by-title-desc'),
    path('sort-by-title-asc/', views.sort_all_recipes_by_title_asc,
         name='sort-all-recipes-by-title-asc'),
    path('sort-by-likes-desc/', views.sort_all_recipes_by_likes_desc,
         name='sort-all-recipes-by-likes-desc'),
    path('sort-by-likes-asc/', views.sort_all_recipes_by_likes_asc,
         name='sort-all-recipes-by-likes-asc'),
]

salads_patterns = [
    path('sort-by-pub-date-desc/', views.sort_salads_by_pub_date_desc,
         name='sort-salads-by-pub-date-desc'),
    path('sort-by-pub-date-asc/', views.sort_salads_by_pub_date_asc,
         name='sort-salads-by-pub-date-asc'),
    path('sort-by-title-desc/', views.sort_salads_by_title_desc,
         name='sort-salads-by-title-desc'),
    path('sort-by-title-asc/', views.sort_salads_by_title_asc,
         name='sort-salads-by-title-asc'),
    path('sort-by-likes-desc/', views.sort_salads_by_likes_desc,
         name='sort-salads-by-likes-desc'),
    path('sort-by-likes-asc/', views.sort_salads_by_likes_asc,
         name='sort-salads-by-likes-asc'),
]

first_courses_patterns = [
    path('sort-by-pub-date-desc/', views.sort_first_courses_by_pub_date_desc,
         name='sort-first-courses-by-pub-date-desc'),
    path('sort-by-pub-date-asc/', views.sort_first_courses_by_pub_date_asc,
         name='sort-first-courses-by-pub-date-asc'),
    path('sort-by-title-desc/', views.sort_first_courses_by_title_desc,
         name='sort-first-courses-by-title-desc'),
    path('sort-by-title-asc/', views.sort_first_courses_by_title_asc,
         name='sort-first-courses-by-title-asc'),
    path('sort-by-likes-desc/', views.sort_first_courses_by_likes_desc,
         name='sort-first-courses-by-likes-desc'),
    path('sort-by-likes-asc/', views.sort_first_courses_by_likes_asc,
         name='sort-first-courses-by-likes-asc'),
]

main_courses_patterns = [
    path('sort-by-pub-date-desc/', views.sort_main_courses_by_pub_date_desc,
         name='sort-main-courses-by-pub-date-desc'),
    path('sort-by-pub-date-asc/', views.sort_main_courses_by_pub_date_asc,
         name='sort-main-courses-by-pub-date-asc'),
    path('sort-by-title-desc/', views.sort_main_courses_by_title_desc,
         name='sort-main-courses-by-title-desc'),
    path('sort-by-title-asc/', views.sort_main_courses_by_title_asc,
         name='sort-main-courses-by-title-asc'),
    path('sort-by-likes-desc/', views.sort_main_courses_by_likes_desc,
         name='sort-main-courses-by-likes-desc'),
    path('sort-by-likes-asc/', views.sort_main_courses_by_likes_asc,
         name='sort-main-courses-by-likes-asc'),
]


bakery_patterns = [
    path('sort-by-pub-date-desc/', views.sort_bakery_by_pub_date_desc,
         name='sort-bakery-by-pub-date-desc'),
    path('sort-by-pub-date-asc/', views.sort_bakery_by_pub_date_asc,
         name='sort-bakery-by-pub-date-asc'),
    path('sort-by-title-desc/', views.sort_bakery_by_title_desc,
         name='sort-bakery-by-title-desc'),
    path('sort-by-title-asc/', views.sort_bakery_by_title_asc,
         name='sort-bakery-by-title-asc'),
    path('sort-by-likes-desc/', views.sort_bakery_by_likes_desc,
         name='sort-bakery-by-likes-desc'),
    path('sort-by-likes-asc/', views.sort_bakery_by_likes_asc,
         name='sort-bakery-by-likes-asc'),
]

desserts_patterns = [
    path('sort-by-pub-date-desc/', views.sort_desserts_by_pub_date_desc,
         name='sort-desserts-by-pub-date-desc'),
    path('sort-by-pub-date-asc/', views.sort_desserts_by_pub_date_asc,
         name='sort-desserts-by-pub-date-asc'),
    path('sort-by-title-desc/', views.sort_desserts_by_title_desc,
         name='sort-desserts-by-title-desc'),
    path('sort-by-title-asc/', views.sort_desserts_by_title_asc,
         name='sort-desserts-by-title-asc'),
    path('sort-by-likes-desc/', views.sort_desserts_by_likes_desc,
         name='sort-desserts-by-likes-desc'),
    path('sort-by-likes-asc/', views.sort_desserts_by_likes_asc,
         name='sort-desserts-by-likes-asc'),
]

beverages_patterns = [
    path('sort-by-pub-date-desc/', views.sort_beverages_by_pub_date_desc,
         name='sort-beverages-by-pub-date-desc'),
    path('sort-by-pub-date-asc/', views.sort_beverages_by_pub_date_asc,
         name='sort-beverages-by-pub-date-asc'),
    path('sort-by-title-desc/', views.sort_beverages_by_title_desc,
         name='sort-beverages-by-title-desc'),
    path('sort-by-title-asc/', views.sort_beverages_by_title_asc,
         name='sort-beverages-by-title-asc'),
    path('sort-by-likes-desc/', views.sort_beverages_by_likes_desc,
         name='sort-beverages-by-likes-desc'),
    path('sort-by-likes-asc/', views.sort_beverages_by_likes_asc,
         name='sort-beverages-by-likes-asc'),
]

urlpatterns = [
    path('all-recipes/', include(all_recipes_patterns)),
    path('salads/', include(salads_patterns)),
    path('first_courses/', include(first_courses_patterns)),
    path('main_courses/', include(main_courses_patterns)),
    path('bakery/', include(bakery_patterns)),
    path('desserts/', include(desserts_patterns)),
    path('beverages/', include(beverages_patterns)),
    ]
