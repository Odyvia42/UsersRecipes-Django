
from django.core.paginator import Paginator
from django.shortcuts import render

from recipeblog.models import User
from recipeblog.utils import check_likes_faves, get_paginated
def get_user_by_id(pk):
    return User.objects.get(id=pk)

def get_all_users_favs(pk):
    return get_user_by_id(pk).recipe_favs.all()


def show_user_favs_all(request, pk):
    user = get_user_by_id(pk)
    fav_recipes = get_all_users_favs(pk)
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})

def show_user_favs_salads(request, pk):
    user = User.objects.get(id=pk)
    fav_recipes = user.recipe_favs.filter(dish_type='SL')
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_salads.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})

def show_user_favs_first_course(request, pk):
    user = User.objects.get(id=pk)
    fav_recipes = user.recipe_favs.filter(dish_type='FC')
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_first_course.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})

def show_user_favs_main_course(request, pk):
    user = User.objects.get(id=pk)
    fav_recipes = user.recipe_favs.filter(dish_type='MC')
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_main_course.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})

def show_user_favs_dessert(request, pk):
    user = User.objects.get(id=pk)
    fav_recipes = user.recipe_favs.filter(dish_type='DS')
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_dessert.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})

def show_user_favs_bakery(request, pk):
    user = User.objects.get(id=pk)
    fav_recipes = user.recipe_favs.filter(dish_type='BK')
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_bakery.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})

def show_user_favs_beverages(request, pk):
    user = User.objects.get(id=pk)
    fav_recipes = user.recipe_favs.filter(dish_type='BV')
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_beverages.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})