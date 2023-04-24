# Блок показа всех рецептов конкретного пользователя
from django.core.paginator import Paginator
from django.shortcuts import render
from recipeblog.models import User, Recipe
from recipeblog.utils import *



def show_user_recipes_all(request, pk):
    user = get_user_by_id(pk)
    user_recipes = get_all_users_recipes(pk)
    check_likes_faves(request, user_recipes)
    paged_recipes = get_paginated(request, user_recipes)
    return render(request, 'user-recipes/user_recipes_all.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_salads(request, pk):
    user = get_user_by_id(pk)
    user_recipes = get_salads(get_all_users_recipes(pk))
    check_likes_faves(request, user_recipes)
    paged_recipes = get_paginated(request, user_recipes)
    return render(request, 'user-recipes/user_recipes_salads.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_first_course(request, pk):
    user = get_user_by_id(pk)
    user_recipes = get_first_courses(get_all_users_recipes(pk))
    check_likes_faves(request, user_recipes)
    paged_recipes = get_paginated(request, user_recipes)
    return render(request, 'user-recipes/user_recipes_first_course.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_main_course(request, pk):
    user = get_user_by_id(pk)
    user_recipes = get_main_courses(get_all_users_recipes(pk))
    check_likes_faves(request, user_recipes)
    paged_recipes = get_paginated(request, user_recipes)
    return render(request, 'user-recipes/user_recipes_main_course.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_dessert(request, pk):
    user = get_user_by_id(pk)
    user_recipes = get_desserts(get_all_users_recipes(pk))
    check_likes_faves(request, user_recipes)
    paged_recipes = get_paginated(request, user_recipes)
    return render(request, 'user-recipes/user_recipes_dessert.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_bakery(request, pk):
    user = get_user_by_id(pk)
    user_recipes = get_bakery(get_all_users_recipes(pk))
    check_likes_faves(request, user_recipes)
    paged_recipes = get_paginated(request, user_recipes)
    return render(request, 'user-recipes/user_recipes_bakery.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_beverages(request, pk):
    user = get_user_by_id(pk)
    user_recipes = get_beverages(get_all_users_recipes(pk))
    check_likes_faves(request, user_recipes)
    paged_recipes = get_paginated(request, user_recipes)
    return render(request, 'user-recipes/user_recipes_beverages.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})