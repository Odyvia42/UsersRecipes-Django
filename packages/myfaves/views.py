from django.core.paginator import Paginator
from django.shortcuts import render


# Блок "Избранное" текущего пользователя

def show_my_favs_all(request):
    if request.user.is_authenticated:
        user = request.user
        fav_recipes = user.recipe_favs.all()
        for recipe in fav_recipes:
            if recipe.likes.filter(id=request.user.id).exists():
                recipe.is_liked = True
            else:
                recipe.is_liked = False
            if recipe.favs.filter(id=request.user.id).exists():
                recipe.is_faved = True
            else:
                recipe.is_faved = False
        p = Paginator(fav_recipes, 5)
        page = request.GET.get('page')
        paged_recipes = p.get_page(page)
        return render(request, 'my-favs/my_favs_all.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_all.html')

def show_my_favs_salads(request):
    if request.user.is_authenticated:
        user = request.user
        fav_recipes = user.recipe_favs.filter(dish_type='SL')
        for recipe in fav_recipes:
            if recipe.likes.filter(id=request.user.id).exists():
                recipe.is_liked = True
            else:
                recipe.is_liked = False
            if recipe.favs.filter(id=request.user.id).exists():
                recipe.is_faved = True
            else:
                recipe.is_faved = False
        p = Paginator(fav_recipes, 5)
        page = request.GET.get('page')
        paged_recipes = p.get_page(page)
        return render(request, 'my-favs/my_favs_salads.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_salads.html')

def show_my_favs_first_course(request):
    if request.user.is_authenticated:
        user = request.user
        fav_recipes = user.recipe_favs.filter(dish_type='FC')
        for recipe in fav_recipes:
            if recipe.likes.filter(id=request.user.id).exists():
                recipe.is_liked = True
            else:
                recipe.is_liked = False
            if recipe.favs.filter(id=request.user.id).exists():
                recipe.is_faved = True
            else:
                recipe.is_faved = False
        p = Paginator(fav_recipes, 5)
        page = request.GET.get('page')
        paged_recipes = p.get_page(page)
        return render(request, 'my-favs/my_favs_first_course.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_first_course.html')

def show_my_favs_main_course(request):
    if request.user.is_authenticated:
        user = request.user
        fav_recipes = user.recipe_favs.filter(dish_type='MC')
        for recipe in fav_recipes:
            if recipe.likes.filter(id=request.user.id).exists():
                recipe.is_liked = True
            else:
                recipe.is_liked = False
            if recipe.favs.filter(id=request.user.id).exists():
                recipe.is_faved = True
            else:
                recipe.is_faved = False
        p = Paginator(fav_recipes, 5)
        page = request.GET.get('page')
        paged_recipes = p.get_page(page)
        return render(request, 'my-favs/my_favs_main_course.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_main_course.html')

def show_my_favs_dessert(request):
    if request.user.is_authenticated:
        user = request.user
        fav_recipes = user.recipe_favs.filter(dish_type='DS')
        for recipe in fav_recipes:
            if recipe.likes.filter(id=request.user.id).exists():
                recipe.is_liked = True
            else:
                recipe.is_liked = False
            if recipe.favs.filter(id=request.user.id).exists():
                recipe.is_faved = True
            else:
                recipe.is_faved = False
        p = Paginator(fav_recipes, 5)
        page = request.GET.get('page')
        paged_recipes = p.get_page(page)
        return render(request, 'my-favs/my_favs_dessert.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_dessert.html')

def show_my_favs_bakery(request):
    if request.user.is_authenticated:
        user = request.user
        fav_recipes = user.recipe_favs.filter(dish_type='BK')
        for recipe in fav_recipes:
            if recipe.likes.filter(id=request.user.id).exists():
                recipe.is_liked = True
            else:
                recipe.is_liked = False
            if recipe.favs.filter(id=request.user.id).exists():
                recipe.is_faved = True
            else:
                recipe.is_faved = False
        p = Paginator(fav_recipes, 5)
        page = request.GET.get('page')
        paged_recipes = p.get_page(page)
        return render(request, 'my-favs/my_favs_bakery.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_bakery.html')

def show_my_favs_beverages(request):
    if request.user.is_authenticated:
        user = request.user
        fav_recipes = user.recipe_favs.filter(dish_type='BV')
        for recipe in fav_recipes:
            if recipe.likes.filter(id=request.user.id).exists():
                recipe.is_liked = True
            else:
                recipe.is_liked = False
            if recipe.favs.filter(id=request.user.id).exists():
                recipe.is_faved = True
            else:
                recipe.is_faved = False
        p = Paginator(fav_recipes, 5)
        page = request.GET.get('page')
        paged_recipes = p.get_page(page)
        return render(request, 'my-favs/my_favs_beverages.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_beverages.html')
