from django.shortcuts import render
from recipeblog.utils import get_all_my_favs, get_paginated, check_likes_faves


# Блок "Избранное" текущего пользователя

def show_my_favs_all(request):
    if request.user.is_authenticated:
        fav_recipes = get_all_my_favs(request)
        check_likes_faves(request, fav_recipes)
        paged_recipes = get_paginated(request, fav_recipes)
        return render(request, 'my-favs/my_favs_all.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_all.html')


def show_my_favs_salads(request):
    if request.user.is_authenticated:
        fav_recipes = get_all_my_favs(request).filter(dish_type='SL')
        check_likes_faves(request, fav_recipes)
        paged_recipes = get_paginated(request, fav_recipes)
        return render(request, 'my-favs/my_favs_salads.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_salads.html')


def show_my_favs_first_course(request):
    if request.user.is_authenticated:
        fav_recipes = get_all_my_favs(request).filter(dish_type='FC')
        check_likes_faves(request, fav_recipes)
        paged_recipes = get_paginated(request, fav_recipes)
        return render(request, 'my-favs/my_favs_first_course.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_first_course.html')


def show_my_favs_main_course(request):
    if request.user.is_authenticated:
        fav_recipes = get_all_my_favs(request).filter(dish_type='MC')
        check_likes_faves(request, fav_recipes)
        paged_recipes = get_paginated(request, fav_recipes)
        return render(request, 'my-favs/my_favs_main_course.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_main_course.html')


def show_my_favs_dessert(request):
    if request.user.is_authenticated:
        fav_recipes = get_all_my_favs(request).filter(dish_type='DS')
        check_likes_faves(request, fav_recipes)
        paged_recipes = get_paginated(request, fav_recipes)
        return render(request, 'my-favs/my_favs_dessert.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_dessert.html')


def show_my_favs_bakery(request):
    if request.user.is_authenticated:
        fav_recipes = get_all_my_favs(request).filter(dish_type='BK')
        check_likes_faves(request, fav_recipes)
        paged_recipes = get_paginated(request, fav_recipes)
        return render(request, 'my-favs/my_favs_bakery.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_bakery.html')


def show_my_favs_beverages(request):
    if request.user.is_authenticated:
        fav_recipes = get_all_my_favs(request).filter(dish_type='BV')
        check_likes_faves(request, fav_recipes)
        paged_recipes = get_paginated(request, fav_recipes)
        return render(request, 'my-favs/my_favs_beverages.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_beverages.html')
