from django.core.paginator import Paginator
from django.db.models import Count, F

from recipeblog.models import Recipe, User


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

def get_all_my_recipes(request):
    return Recipe.objects.filter(author=request.user)

def order_by_pub_date_desc(queryset):
    return queryset.order_by(F('publication_date').desc())

def order_by_pub_date_asc(queryset):
    return queryset.order_by(F('publication_date').asc())

def order_by_title_desc(queryset):
    return queryset.order_by(F('title').desc())

def order_by_title_asc(queryset):
    return queryset.order_by(F('title').asc())


def order_by_likes_amount_desc(queryset):
    return queryset.annotate(likes_amount=Count('likes')).order_by(F('likes_amount').desc())

def order_by_likes_amount_asc(queryset):
    return queryset.annotate(likes_amount=Count('likes')).order_by(F('likes_amount').asc())

def get_salads(queryset):
    return queryset.filter(dish_type='SL')

def get_first_courses(queryset):
    return queryset.filter(dish_type='FC')

def get_main_courses(queryset):
    return queryset.filter(dish_type='MC')

def get_bakery(queryset):
    return queryset.filter(dish_type='BK')

def get_desserts(queryset):
    return queryset.filter(dish_type='DS')

def get_beverages(queryset):
    return queryset.filter(dish_type='BV')

def get_all_users():
    return User.objects.annotate(num_recipes=Count('recipe', distinct=True)).annotate(likes_amount=Count('recipe__likes'))

def get_user_by_id(pk):
    return User.objects.get(id=pk)

def get_all_users_favs(pk):
    return get_user_by_id(pk).recipe_favs.all()

def get_all_users_recipes(pk):
    return Recipe.objects.filter(author=get_user_by_id(pk))