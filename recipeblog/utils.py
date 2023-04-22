from django.core.paginator import Paginator


def get_all_my_favs(request):
    return request.user.recipe_favs.all()

def get_paginated(request, queryset):
    p = Paginator(queryset, 5)
    page = request.GET.get('page')
    return p.get_page(page)

def check_likes_faves(request, queryset):
    for recipe in queryset:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    return queryset

def get_liked_recipes(request):
    return request.user.recipe_likes.all()