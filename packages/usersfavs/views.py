
from django.core.paginator import Paginator
from django.shortcuts import render

from recipeblog.models import User

def get_user_by_id(pk):
    return User.objects.get(id=pk)


def show_user_favs_all(request, pk):
    user = get_user_by_id(pk)
    fav_recipes = user.recipe_favs.all()
    for fav_recipe in fav_recipes:
        if fav_recipe.likes.filter(id=request.user.id).exists():
            fav_recipe.is_liked = True
        else:
            fav_recipe.is_liked = False
        if fav_recipe.favs.filter(id=request.user.id).exists():
            fav_recipe.is_faved = True
        else:
            fav_recipe.is_faved = False
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
    for fav_recipe in fav_recipes:
        if fav_recipe.likes.filter(id=request.user.id).exists():
            fav_recipe.is_liked = True
        else:
            fav_recipe.is_liked = False
        if fav_recipe.favs.filter(id=request.user.id).exists():
            fav_recipe.is_faved = True
        else:
            fav_recipe.is_faved = False
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
    for fav_recipe in fav_recipes:
        if fav_recipe.likes.filter(id=request.user.id).exists():
            fav_recipe.is_liked = True
        else:
            fav_recipe.is_liked = False
        if fav_recipe.favs.filter(id=request.user.id).exists():
            fav_recipe.is_faved = True
        else:
            fav_recipe.is_faved = False
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
    for fav_recipe in fav_recipes:
        if fav_recipe.likes.filter(id=request.user.id).exists():
            fav_recipe.is_liked = True
        else:
            fav_recipe.is_liked = False
        if fav_recipe.favs.filter(id=request.user.id).exists():
            fav_recipe.is_faved = True
        else:
            fav_recipe.is_faved = False
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
    for fav_recipe in fav_recipes:
        if fav_recipe.likes.filter(id=request.user.id).exists():
            fav_recipe.is_liked = True
        else:
            fav_recipe.is_liked = False
        if fav_recipe.favs.filter(id=request.user.id).exists():
            fav_recipe.is_faved = True
        else:
            fav_recipe.is_faved = False
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
    for fav_recipe in fav_recipes:
        if fav_recipe.likes.filter(id=request.user.id).exists():
            fav_recipe.is_liked = True
        else:
            fav_recipe.is_liked = False
        if fav_recipe.favs.filter(id=request.user.id).exists():
            fav_recipe.is_faved = True
        else:
            fav_recipe.is_faved = False
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
    for fav_recipe in fav_recipes:
        if fav_recipe.likes.filter(id=request.user.id).exists():
            fav_recipe.is_liked = True
        else:
            fav_recipe.is_liked = False
        if fav_recipe.favs.filter(id=request.user.id).exists():
            fav_recipe.is_faved = True
        else:
            fav_recipe.is_faved = False
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'user-favs/user_favs_beverages.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})