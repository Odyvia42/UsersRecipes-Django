from django.shortcuts import render
from recipeblog.utils import *


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
    user = get_user_by_id(pk)
    fav_recipes = get_salads(get_all_users_favs(pk))
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_salads.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})


def show_user_favs_first_course(request, pk):
    user = get_user_by_id(pk)
    fav_recipes = get_first_courses(get_all_users_favs(pk))
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_first_course.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})


def show_user_favs_main_course(request, pk):
    user = get_user_by_id(pk)
    fav_recipes = get_main_courses(get_all_users_favs(pk))
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_main_course.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})


def show_user_favs_dessert(request, pk):
    user = get_user_by_id(pk)
    fav_recipes = get_desserts(get_all_users_favs(pk))
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_dessert.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})


def show_user_favs_bakery(request, pk):
    user = get_user_by_id(pk)
    fav_recipes = get_bakery(get_all_users_favs(pk))
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_bakery.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})


def show_user_favs_beverages(request, pk):
    user = get_user_by_id(pk)
    fav_recipes = get_beverages(get_all_users_favs(pk))
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_beverages.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})
