from django.core.paginator import Paginator
from django.shortcuts import render


# Блок "Понравилось" текущего пользователя

def show_my_likes_all(request):
    user = request.user
    liked_recipes = user.recipe_likes.all()
    for recipe in liked_recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(liked_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-likes/my_likes_all.html',
                  {'paged_recipes': paged_recipes,
                   'liked_recipes': liked_recipes})

def show_my_likes_salads(request):
    user = request.user
    liked_recipes = user.recipe_likes.filter(dish_type='SL')
    for recipe in liked_recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(liked_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-likes/my_likes_salads.html',
                  {'paged_recipes': paged_recipes,
                   'liked_recipes': liked_recipes})

def show_my_likes_first_course(request):
    user = request.user
    liked_recipes = user.recipe_likes.filter(dish_type='FC')
    for recipe in liked_recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(liked_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-likes/my_likes_first_course.html',
                  {'paged_recipes': paged_recipes,
                   'liked_recipes': liked_recipes})

def show_my_likes_main_course(request):
    user = request.user
    liked_recipes = user.recipe_likes.filter(dish_type='MC')
    for recipe in liked_recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(liked_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-likes/my_likes_main_course.html',
                  {'paged_recipes': paged_recipes,
                   'liked_recipes': liked_recipes})

def show_my_likes_dessert(request):
    user = request.user
    liked_recipes = user.recipe_likes.filter(dish_type='DS')
    for recipe in liked_recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(liked_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-likes/my_likes_dessert.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': liked_recipes})

def show_my_likes_bakery(request):
    user = request.user
    liked_recipes = user.recipe_likes.filter(dish_type='BK')
    for recipe in liked_recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(liked_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-likes/my_likes_bakery.html',
                  {'paged_recipes': paged_recipes,
                   'liked_recipes': liked_recipes})

def show_my_likes_beverages(request):
    user = request.user
    liked_recipes = user.recipe_likes.filter(dish_type='BV')
    for recipe in liked_recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(liked_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-likes/my_likes_beverages.html',
                  {'paged_recipes': paged_recipes,
                   'liked_recipes': liked_recipes})
