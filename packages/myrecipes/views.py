# Блок "Мои рецепты"
from django.core.paginator import Paginator
from django.shortcuts import render

from recipeblog.models import Recipe


def show_my_recipes_all(request):
    user = request.user
    my_recipes = Recipe.objects.filter(author=user)
    p = Paginator(my_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-recipes/my_recipes_all.html',
                  {'paged_recipes': paged_recipes,
                   'my_recipes': my_recipes})

def show_my_recipes_salads(request):
    user = request.user
    my_recipes = Recipe.objects.filter(author=user).filter(dish_type='SL')
    p = Paginator(my_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-recipes/my_recipes_salads.html',
                  {'paged_recipes': paged_recipes,
                   'my_recipes': my_recipes})

def show_my_recipes_first_course(request):
    user = request.user
    my_recipes = Recipe.objects.filter(author=user).filter(dish_type='FC')
    p = Paginator(my_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-recipes/my_recipes_first_course.html',
                  {'paged_recipes': paged_recipes,
                   'my_recipes': my_recipes})

def show_my_recipes_main_course(request):
    user = request.user
    my_recipes = Recipe.objects.filter(author=user).filter(dish_type='MC')
    p = Paginator(my_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-recipes/my_recipes_main_course.html',
                  {'paged_recipes': paged_recipes,
                   'my_recipes': my_recipes})

def show_my_recipes_dessert(request):
    user = request.user
    my_recipes = Recipe.objects.filter(author=user).filter(dish_type='DS')
    p = Paginator(my_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-recipes/my_recipes_dessert.html',
                  {'paged_recipes': paged_recipes,
                   'my_recipes': my_recipes})

def show_my_recipes_bakery(request):
    user = request.user
    my_recipes = Recipe.objects.filter(author=user).filter(dish_type='BK')
    p = Paginator(my_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-recipes/my_recipes_bakery.html',
                  {'paged_recipes': paged_recipes,
                   'my_recipes': my_recipes})

def show_my_recipes_beverages(request):
    user = request.user
    my_recipes = Recipe.objects.filter(author=user).filter(dish_type='BV')
    p = Paginator(my_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-recipes/my_recipes_beverages.html',
                  {'paged_recipes': paged_recipes,
                   'my_recipes': my_recipes})