
from django.core.paginator import Paginator
from django.shortcuts import render

from recipeblog.models import User


def show_user_favs_all(request, pk):
    user = User.objects.get(id=pk)
    fav_recipes = user.recipe_favs.all()
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-favs/user_favs.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})

def show_user_favs_salads(request, pk):
    user = User.objects.get(id=pk)
    fav_recipes = user.recipe_favs.filter(dish_type='SL')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-favs/user_favs_salads.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})

def show_user_favs_first_course(request, pk):
    user = User.objects.get(id=pk)
    fav_recipes = user.recipe_favs.filter(dish_type='FC')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-favs/user_favs_first_course.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})

def show_user_favs_main_course(request, pk):
    user = User.objects.get(id=pk)
    fav_recipes = user.recipe_favs.filter(dish_type='MC')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-favs/user_favs_main_course.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})

def show_user_favs_dessert(request, pk):
    user = User.objects.get(id=pk)
    fav_recipes = user.recipe_favs.filter(dish_type='DS')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-favs/user_favs_dessert.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})

def show_user_favs_bakery(request, pk):
    user = User.objects.get(id=pk)
    fav_recipes = user.recipe_favs.filter(dish_type='BK')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-favs/user_favs_bakery.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})

def show_user_favs_beverages(request, pk):
    user = User.objects.get(id=pk)
    fav_recipes = user.recipe_favs.filter(dish_type='BV')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-favs/user_favs_beverages.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})