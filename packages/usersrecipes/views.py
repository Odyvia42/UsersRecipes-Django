# Блок показа всех рецептов конкретного пользователя
from django.core.paginator import Paginator
from django.shortcuts import render

from recipeblog.models import User, Recipe


def show_user_recipes_all(request, pk):
    user = User.objects.get(id=pk)
    user_recipes = Recipe.objects.filter(author=user)
    p = Paginator(user_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-recipes/user_recipes_all.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_salads(request, pk):
    user = User.objects.get(id=pk)
    user_recipes = Recipe.objects.filter(author=user).filter(dish_type='SL')
    p = Paginator(user_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-recipes/user_recipes_salads.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_first_course(request, pk):
    user = User.objects.get(id=pk)
    user_recipes = Recipe.objects.filter(author=user).filter(dish_type='FC')
    p = Paginator(user_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-recipes/user_recipes_first_course.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_main_course(request, pk):
    user = User.objects.get(id=pk)
    user_recipes = Recipe.objects.filter(author=user).filter(dish_type='MC')
    p = Paginator(user_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-recipes/user_recipes_main_course.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_dessert(request, pk):
    user = User.objects.get(id=pk)
    user_recipes = Recipe.objects.filter(author=user).filter(dish_type='DS')
    p = Paginator(user_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-recipes/user_recipes_dessert.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_bakery(request, pk):
    user = User.objects.get(id=pk)
    user_recipes = Recipe.objects.filter(author=user).filter(dish_type='BK')
    p = Paginator(user_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-recipes/user_recipes_bakery.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_beverages(request, pk):
    user = User.objects.get(id=pk)
    user_recipes = Recipe.objects.filter(author=user).filter(dish_type='BV')
    p = Paginator(user_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-recipes/user_recipes_beverages.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})