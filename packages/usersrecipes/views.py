# Блок показа всех рецептов конкретного пользователя
from django.core.paginator import Paginator
from django.shortcuts import render
from recipeblog.models import User, Recipe
from recipeblog.utils import *



def show_user_recipes_all(request, pk):
    user = get_user_by_id(pk)
    user_recipes = get_all_users_recipes(pk)
    for user_recipe in user_recipes:
        if user_recipe.likes.filter(id=request.user.id).exists():
            user_recipe.is_liked = True
        else:
            user_recipe.is_liked = False
        if user_recipe.favs.filter(id=request.user.id).exists():
            user_recipe.is_faved = True
        else:
            user_recipe.is_faved = False
    p = Paginator(user_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-recipes/user_recipes_all.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_salads(request, pk):
    user = get_user_by_id(pk)
    user_recipes = Recipe.objects.filter(author=user).filter(dish_type='SL')
    for user_recipe in user_recipes:
        if user_recipe.likes.filter(id=request.user.id).exists():
            user_recipe.is_liked = True
        else:
            user_recipe.is_liked = False
        if user_recipe.favs.filter(id=request.user.id).exists():
            user_recipe.is_faved = True
        else:
            user_recipe.is_faved = False
    p = Paginator(user_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-recipes/user_recipes_salads.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_first_course(request, pk):
    user = get_user_by_id(pk)
    user_recipes = Recipe.objects.filter(author=user).filter(dish_type='FC')
    for user_recipe in user_recipes:
        if user_recipe.likes.filter(id=request.user.id).exists():
            user_recipe.is_liked = True
        else:
            user_recipe.is_liked = False
        if user_recipe.favs.filter(id=request.user.id).exists():
            user_recipe.is_faved = True
        else:
            user_recipe.is_faved = False
    p = Paginator(user_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-recipes/user_recipes_first_course.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_main_course(request, pk):
    user = get_user_by_id(pk)
    user_recipes = Recipe.objects.filter(author=user).filter(dish_type='MC')
    for user_recipe in user_recipes:
        if user_recipe.likes.filter(id=request.user.id).exists():
            user_recipe.is_liked = True
        else:
            user_recipe.is_liked = False
        if user_recipe.favs.filter(id=request.user.id).exists():
            user_recipe.is_faved = True
        else:
            user_recipe.is_faved = False
    p = Paginator(user_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-recipes/user_recipes_main_course.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_dessert(request, pk):
    user = get_user_by_id(pk)
    user_recipes = Recipe.objects.filter(author=user).filter(dish_type='DS')
    for user_recipe in user_recipes:
        if user_recipe.likes.filter(id=request.user.id).exists():
            user_recipe.is_liked = True
        else:
            user_recipe.is_liked = False
        if user_recipe.favs.filter(id=request.user.id).exists():
            user_recipe.is_faved = True
        else:
            user_recipe.is_faved = False
    p = Paginator(user_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-recipes/user_recipes_dessert.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_bakery(request, pk):
    user = get_user_by_id(pk)
    user_recipes = Recipe.objects.filter(author=user).filter(dish_type='BK')
    for user_recipe in user_recipes:
        if user_recipe.likes.filter(id=request.user.id).exists():
            user_recipe.is_liked = True
        else:
            user_recipe.is_liked = False
        if user_recipe.favs.filter(id=request.user.id).exists():
            user_recipe.is_faved = True
        else:
            user_recipe.is_faved = False
    p = Paginator(user_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-recipes/user_recipes_bakery.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})

def show_user_recipes_beverages(request, pk):
    user = get_user_by_id(pk)
    user_recipes = Recipe.objects.filter(author=user).filter(dish_type='BV')
    for user_recipe in user_recipes:
        if user_recipe.likes.filter(id=request.user.id).exists():
            user_recipe.is_liked = True
        else:
            user_recipe.is_liked = False
        if user_recipe.favs.filter(id=request.user.id).exists():
            user_recipe.is_faved = True
        else:
            user_recipe.is_faved = False
    p = Paginator(user_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-recipes/user_recipes_beverages.html',
                  {'paged_recipes': paged_recipes,
                   'user_recipes': user_recipes,
                   'user': user})