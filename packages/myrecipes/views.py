from django.shortcuts import render
from recipeblog.utils import get_all_my_recipes, check_likes_faves, get_paginated


def show_my_recipes_all(request):
    if request.user.is_authenticated:
        my_recipes = get_all_my_recipes(request)
        check_likes_faves(request, my_recipes)
        paged_recipes = get_paginated(request, my_recipes)
        return render(request, 'my-recipes/my_recipes_all.html',
                      {'paged_recipes': paged_recipes,
                       'my_recipes': my_recipes})
    else:
        return render(request, 'my-recipes/my_recipes_all.html')


def show_my_recipes_salads(request):
    if request.user.is_authenticated:
        my_recipes = get_all_my_recipes(request).filter(dish_type='SL')
        check_likes_faves(request, my_recipes)
        paged_recipes = get_paginated(request, my_recipes)
        return render(request, 'my-recipes/my_recipes_salads.html',
                      {'paged_recipes': paged_recipes,
                       'my_recipes': my_recipes})
    else:
        return render(request, 'my-recipes/my_recipes_salads.html')


def show_my_recipes_first_course(request):
    if request.user.is_authenticated:
        my_recipes = get_all_my_recipes(request).filter(dish_type='FC')
        check_likes_faves(request, my_recipes)
        paged_recipes = get_paginated(request, my_recipes)
        return render(request, 'my-recipes/my_recipes_first_course.html',
                      {'paged_recipes': paged_recipes,
                       'my_recipes': my_recipes})
    else:
        return render(request, 'my-recipes/my_recipes_first_course.html')


def show_my_recipes_main_course(request):
    if request.user.is_authenticated:
        my_recipes = get_all_my_recipes(request).filter(dish_type='MC')
        check_likes_faves(request, my_recipes)
        paged_recipes = get_paginated(request, my_recipes)
        return render(request, 'my-recipes/my_recipes_main_course.html',
                      {'paged_recipes': paged_recipes,
                       'my_recipes': my_recipes})
    else:
        return render(request, 'my-recipes/my_recipes_main_course.html')


def show_my_recipes_dessert(request):
    if request.user.is_authenticated:
        my_recipes = get_all_my_recipes(request).filter(dish_type='DS')
        check_likes_faves(request, my_recipes)
        paged_recipes = get_paginated(request, my_recipes)
        return render(request, 'my-recipes/my_recipes_dessert.html',
                      {'paged_recipes': paged_recipes,
                       'my_recipes': my_recipes})
    else:
        return render(request, 'my-recipes/my_recipes_dessert.html')


def show_my_recipes_bakery(request):
    if request.user.is_authenticated:
        my_recipes = get_all_my_recipes(request).filter(dish_type='BK')
        check_likes_faves(request, my_recipes)
        paged_recipes = get_paginated(request, my_recipes)
        return render(request, 'my-recipes/my_recipes_bakery.html',
                      {'paged_recipes': paged_recipes,
                       'my_recipes': my_recipes})
    else:
        return render(request, 'my-recipes/my_recipes_bakery.html')


def show_my_recipes_beverages(request):
    if request.user.is_authenticated:
        my_recipes = get_all_my_recipes(request).filter(dish_type='BV')
        check_likes_faves(request, my_recipes)
        paged_recipes = get_paginated(request, my_recipes)
        return render(request, 'my-recipes/my_recipes_beverages.html',
                      {'paged_recipes': paged_recipes,
                       'my_recipes': my_recipes})
    else:
        return render(request, 'my-recipes/my_recipes_beverages.html')
