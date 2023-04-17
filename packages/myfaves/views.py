from django.core.paginator import Paginator
from django.shortcuts import render


# Блок "Избранное" текущего пользователя

def show_my_favs_all(request):
    user = request.user
    fav_recipes = user.recipe_favs.all()
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-favs/my_favs_all.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes})

def show_my_favs_salads(request):
    user = request.user
    fav_recipes = user.recipe_favs.filter(dish_type='SL')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-favs/my_favs_salads.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes})

def show_my_favs_first_course(request):
    user = request.user
    fav_recipes = user.recipe_favs.filter(dish_type='FC')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-favs/my_favs_first_course.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes})

def show_my_favs_main_course(request):
    user = request.user
    fav_recipes = user.recipe_favs.filter(dish_type='MC')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-favs/my_favs_main_course.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes})

def show_my_favs_dessert(request):
    user = request.user
    fav_recipes = user.recipe_favs.filter(dish_type='DS')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-favs/my_favs_dessert.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes})

def show_my_favs_bakery(request):
    user = request.user
    fav_recipes = user.recipe_favs.filter(dish_type='BK')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-favs/my_favs_bakery.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes})

def show_my_favs_beverages(request):
    user = request.user
    fav_recipes = user.recipe_favs.filter(dish_type='BV')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-favs/my_favs_beverages.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes})
