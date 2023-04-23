
from django.shortcuts import render
from recipeblog.utils import *


# все рецепты
def sort_all_recipes_by_pub_date_desc(request):
    recipes = order_by_pub_date_desc(Recipe.objects.all())
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_all_recipes_by_pub_date_asc(request):
    recipes = order_by_pub_date_asc(Recipe.objects.all())
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_all_recipes_by_title_desc(request):
    recipes = order_by_title_desc(Recipe.objects.all())
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_all_recipes_by_title_asc(request):
    recipes = order_by_title_asc(Recipe.objects.all())
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_title_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_all_recipes_by_likes_desc(request):
    recipes = order_by_likes_amount_desc(Recipe.objects.all())
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_likes_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_all_recipes_by_likes_asc(request):
    recipes = order_by_likes_amount_asc(Recipe.objects.all())
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_likes_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


# салаты
def sort_salads_by_pub_date_desc(request):
    recipes = get_salads(order_by_pub_date_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/salads/sort_salads_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_salads_by_pub_date_asc(request):
    recipes = get_salads(order_by_pub_date_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/salads/sort_salads_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_salads_by_title_desc(request):
    recipes = get_salads(order_by_title_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/salads/sort_salads_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_salads_by_title_asc(request):
    recipes = get_salads(order_by_title_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/salads/sort_salads_by_title_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_salads_by_likes_desc(request):
    recipes = get_salads(order_by_likes_amount_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/salads/sort_salads_by_likes_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_salads_by_likes_asc(request):
    recipes = get_salads(order_by_likes_amount_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/salads/sort_salads_by_likes_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


# первые блюда
def sort_first_courses_by_pub_date_desc(request):
    recipes = get_first_courses(order_by_pub_date_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/first-course/sort_first_courses_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_first_courses_by_pub_date_asc(request):
    recipes = get_first_courses(order_by_pub_date_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/first-course/sort_first_courses_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_first_courses_by_title_desc(request):
    recipes = get_first_courses(order_by_title_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/first-course/sort_first_courses_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_first_courses_by_title_asc(request):
    recipes = get_first_courses(order_by_title_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/first-course/sort_first_courses_by_title_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_first_courses_by_likes_desc(request):
    recipes = get_first_courses(order_by_likes_amount_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/first-course/sort_first_courses_by_likes_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_first_courses_by_likes_asc(request):
    recipes = get_first_courses(order_by_likes_amount_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/first-course/sort_first_courses_by_likes_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


# вторые блюда
def sort_main_courses_by_pub_date_desc(request):
    recipes = get_main_courses(order_by_pub_date_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/main-course/sort_main_courses_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_main_courses_by_pub_date_asc(request):
    recipes = get_main_courses(order_by_pub_date_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/main-course/sort_main_courses_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_main_courses_by_title_desc(request):
    recipes = get_main_courses(order_by_title_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/main-course/sort_main_courses_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_main_courses_by_title_asc(request):
    recipes = get_main_courses(order_by_title_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/main-course/sort_main_courses_by_title_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_main_courses_by_likes_desc(request):
    recipes = get_main_courses(order_by_likes_amount_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/main-course/sort_main_courses_by_likes_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_main_courses_by_likes_asc(request):
    recipes = get_main_courses(order_by_likes_amount_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/main-course/sort_main_courses_by_likes_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


# выпечка
def sort_bakery_by_pub_date_desc(request):
    recipes = get_bakery(order_by_pub_date_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/bakery/sort_bakery_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_bakery_by_pub_date_asc(request):
    recipes = get_bakery(order_by_pub_date_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/bakery/sort_bakery_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_bakery_by_title_desc(request):
    recipes = get_bakery(order_by_title_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/bakery/sort_bakery_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_bakery_by_title_asc(request):
    recipes = get_bakery(order_by_title_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/bakery/sort_bakery_by_title_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_bakery_by_likes_desc(request):
    recipes = get_bakery(order_by_likes_amount_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/bakery/sort_bakery_by_likes_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_bakery_by_likes_asc(request):
    recipes = get_bakery(order_by_likes_amount_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/bakery/sort_bakery_by_likes_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


# десерты
def sort_desserts_by_pub_date_desc(request):
    recipes = get_desserts(order_by_pub_date_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/desserts/sort_desserts_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_desserts_by_pub_date_asc(request):
    recipes = get_desserts(order_by_pub_date_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/desserts/sort_desserts_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_desserts_by_title_desc(request):
    recipes = get_desserts(order_by_title_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/desserts/sort_desserts_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_desserts_by_title_asc(request):
    recipes = get_desserts(order_by_title_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/desserts/sort_desserts_by_title_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_desserts_by_likes_desc(request):
    recipes = get_desserts(order_by_likes_amount_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/desserts/sort_desserts_by_likes_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_desserts_by_likes_asc(request):
    recipes = get_desserts(order_by_likes_amount_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/desserts/sort_desserts_by_likes_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


# напитки
def sort_beverages_by_pub_date_desc(request):
    recipes = get_beverages(order_by_pub_date_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/beverages/sort_beverages_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_beverages_by_pub_date_asc(request):
    recipes = get_beverages(order_by_pub_date_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/beverages/sort_beverages_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_beverages_by_title_desc(request):
    recipes = get_beverages(order_by_title_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/beverages/sort_beverages_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_beverages_by_title_asc(request):
    recipes = get_beverages(order_by_title_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/beverages/sort_beverages_by_title_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_beverages_by_likes_desc(request):
    recipes = get_beverages(order_by_likes_amount_desc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/beverages/sort_beverages_by_likes_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_beverages_by_likes_asc(request):
    recipes = get_beverages(order_by_likes_amount_asc(Recipe.objects.all()))
    check_likes_faves(request, recipes)
    paged_recipes = get_paginated(request, recipes)
    return render(request, 'recipe-list/beverages/sort_beverages_by_likes_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })
