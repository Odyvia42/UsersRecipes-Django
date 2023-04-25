from django.shortcuts import render
from recipeblog.utils import check_likes_faves, get_paginated, get_liked_recipes


def show_my_likes_all(request):
    if request.user.is_authenticated:
        liked_recipes = get_liked_recipes(request)
        check_likes_faves(request, liked_recipes)
        paged_recipes = get_paginated(request, liked_recipes)
        return render(request, 'my-likes/my_likes_all.html',
                      {'paged_recipes': paged_recipes,
                       'liked_recipes': liked_recipes})
    else:
        return render(request, 'my-likes/my_likes_all.html')

def show_my_likes_salads(request):
    if request.user.is_authenticated:
        liked_recipes = get_liked_recipes(request).filter(dish_type='SL')
        check_likes_faves(request, liked_recipes)
        paged_recipes = get_paginated(request, liked_recipes)
        return render(request, 'my-likes/my_likes_salads.html',
                      {'paged_recipes': paged_recipes,
                       'liked_recipes': liked_recipes})
    else:
        return render(request, 'my-likes/my_likes_salads.html')

def show_my_likes_first_course(request):
    if request.user.is_authenticated:
        liked_recipes = get_liked_recipes(request).filter(dish_type='FC')
        check_likes_faves(request, liked_recipes)
        paged_recipes = get_paginated(request, liked_recipes)
        return render(request, 'my-likes/my_likes_first_course.html',
                      {'paged_recipes': paged_recipes,
                       'liked_recipes': liked_recipes})
    else:
        return render(request, 'my-likes/my_likes_first_course.html')

def show_my_likes_main_course(request):
    if request.user.is_authenticated:
        liked_recipes = get_liked_recipes(request).filter(dish_type='MC')
        check_likes_faves(request, liked_recipes)
        paged_recipes = get_paginated(request, liked_recipes)
        return render(request, 'my-likes/my_likes_main_course.html',
                      {'paged_recipes': paged_recipes,
                       'liked_recipes': liked_recipes})
    else:
        return render(request, 'my-likes/my_likes_main_course.html')

def show_my_likes_dessert(request):
    if request.user.is_authenticated:
        liked_recipes = get_liked_recipes(request).filter(dish_type='DS')
        check_likes_faves(request, liked_recipes)
        paged_recipes = get_paginated(request, liked_recipes)
        return render(request, 'my-likes/my_likes_dessert.html',
                      {'paged_recipes': paged_recipes,
                       'liked_recipes': liked_recipes})
    else:
        return render(request, 'my-likes/my_likes_dessert.html')

def show_my_likes_bakery(request):
    if request.user.is_authenticated:
        liked_recipes = get_liked_recipes(request).filter(dish_type='BK')
        check_likes_faves(request, liked_recipes)
        paged_recipes = get_paginated(request, liked_recipes)
        return render(request, 'my-likes/my_likes_bakery.html',
                      {'paged_recipes': paged_recipes,
                       'liked_recipes': liked_recipes})
    else:
        return render(request, 'my-likes/my_likes_bakery.html')

def show_my_likes_beverages(request):
    if request.user.is_authenticated:
        liked_recipes = get_liked_recipes(request).filter(dish_type='BV')
        check_likes_faves(request, liked_recipes)
        paged_recipes = get_paginated(request, liked_recipes)
        return render(request, 'my-likes/my_likes_beverages.html',
                      {'paged_recipes': paged_recipes,
                       'liked_recipes': liked_recipes})
    else:
        return render(request, 'my-likes/my_likes_beverages.html')
