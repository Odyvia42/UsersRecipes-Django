# представления для сортировки списка рецептов, основная категоризация по типу блюда
from django.core.paginator import Paginator
from django.db.models import F, Count
from django.shortcuts import render

from recipeblog.models import Recipe

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

# все рецепты
def sort_all_recipes_by_pub_date_desc(request):
    recipes = order_by_pub_date_desc(Recipe.objects.all())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })
def sort_all_recipes_by_pub_date_asc(request):
    recipes = order_by_pub_date_asc(Recipe.objects.all())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_all_recipes_by_title_desc(request):
    recipes = order_by_title_desc(Recipe.objects.all())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })
def sort_all_recipes_by_title_asc(request):
    recipes = order_by_title_desc(Recipe.objects.all())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_title_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_all_recipes_by_likes_desc(request):
    recipes = order_by_likes_amount_desc(Recipe.objects.all())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_likes_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })
def sort_all_recipes_by_likes_asc(request):
    recipes = order_by_likes_amount_asc(Recipe.objects.all())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_likes_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

# салаты
def sort_salads_by_pub_date_desc(request):
    recipes = Recipe.objects.filter(dish_type='SL').order_by(F('publication_date').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/salads/sort_salads_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_salads_by_pub_date_asc(request):
    recipes = Recipe.objects.filter(dish_type='SL').order_by(F('publication_date').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/salads/sort_salads_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_salads_by_title_desc(request):
    recipes = Recipe.objects.filter(dish_type='SL').order_by(F('title').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/salads/sort_salads_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_salads_by_title_asc(request):
    recipes = Recipe.objects.filter(dish_type='SL').order_by(F('title').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/salads/sort_salads_by_title_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_salads_by_likes_desc(request):
    recipes = Recipe.objects.filter(dish_type='SL').annotate(likes_amount=Count('likes')).order_by(
        F('likes_amount').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/salads/sort_salads_by_likes_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_salads_by_likes_asc(request):
    recipes = Recipe.objects.filter(dish_type='SL').annotate(likes_amount=Count('likes')).order_by(
        F('likes_amount').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/salads/sort_salads_by_likes_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

# первые блюда

def sort_first_courses_by_pub_date_desc(request):
    recipes = Recipe.objects.filter(dish_type='FC').order_by(F('publication_date').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/first-course/sort_first_courses_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_first_courses_by_pub_date_asc(request):
    recipes = Recipe.objects.filter(dish_type='FC').order_by(F('publication_date').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/first-course/sort_first_courses_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_first_courses_by_title_desc(request):
    recipes = Recipe.objects.filter(dish_type='FC').order_by(F('title').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/first-course/sort_first_courses_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_first_courses_by_title_asc(request):
    recipes = Recipe.objects.filter(dish_type='FC').order_by(F('title').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/first-course/sort_first_courses_by_title_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_first_courses_by_likes_desc(request):
    recipes = Recipe.objects.filter(dish_type='FC').annotate(likes_amount=Count('likes')).order_by(
        F('likes_amount').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/first-course/sort_first_courses_by_likes_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_first_courses_by_likes_asc(request):
    recipes = Recipe.objects.filter(dish_type='FC').annotate(likes_amount=Count('likes')).order_by(
        F('likes_amount').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/first-course/sort_first_courses_by_likes_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

# вторые блюда

def sort_main_courses_by_pub_date_desc(request):
    recipes = Recipe.objects.filter(dish_type='MC').order_by(F('publication_date').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/main-course/sort_main_courses_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_main_courses_by_pub_date_asc(request):
    recipes = Recipe.objects.filter(dish_type='MC').order_by(F('publication_date').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/main-course/sort_main_courses_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_main_courses_by_title_desc(request):
    recipes = Recipe.objects.filter(dish_type='MC').order_by(F('title').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/main-course/sort_main_courses_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_main_courses_by_title_asc(request):
    recipes = Recipe.objects.filter(dish_type='MC').order_by(F('title').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/main-course/sort_main_courses_by_title_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_main_courses_by_likes_desc(request):
    recipes = Recipe.objects.filter(dish_type='MC').annotate(likes_amount=Count('likes')).order_by(
        F('likes_amount').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/main-course/sort_main_courses_by_likes_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_main_courses_by_likes_asc(request):
    recipes = Recipe.objects.filter(dish_type='MC').annotate(likes_amount=Count('likes')).order_by(
        F('likes_amount').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/main-course/sort_main_courses_by_likes_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

# выпечка

def sort_bakery_by_pub_date_desc(request):
    recipes = Recipe.objects.filter(dish_type='BK').order_by(F('publication_date').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/bakery/sort_bakery_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_bakery_by_pub_date_asc(request):
    recipes = Recipe.objects.filter(dish_type='BK').order_by(F('publication_date').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/bakery/sort_bakery_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_bakery_by_title_desc(request):
    recipes = Recipe.objects.filter(dish_type='BK').order_by(F('title').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/bakery/sort_bakery_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_bakery_by_title_asc(request):
    recipes = Recipe.objects.filter(dish_type='BK').order_by(F('title').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/bakery/sort_bakery_by_title_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_bakery_by_likes_desc(request):
    recipes = Recipe.objects.filter(dish_type='BK').annotate(likes_amount=Count('likes')).order_by(
        F('likes_amount').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/bakery/sort_bakery_by_likes_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_bakery_by_likes_asc(request):
    recipes = Recipe.objects.filter(dish_type='BK').annotate(likes_amount=Count('likes')).order_by(
        F('likes_amount').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/bakery/sort_bakery_by_likes_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

# десерты

def sort_desserts_by_pub_date_desc(request):
    recipes = Recipe.objects.filter(dish_type='DS').order_by(F('publication_date').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/desserts/sort_desserts_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_desserts_by_pub_date_asc(request):
    recipes = Recipe.objects.filter(dish_type='DS').order_by(F('publication_date').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/desserts/sort_desserts_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_desserts_by_title_desc(request):
    recipes = Recipe.objects.filter(dish_type='DS').order_by(F('title').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/desserts/sort_desserts_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_desserts_by_title_asc(request):
    recipes = Recipe.objects.filter(dish_type='DS').order_by(F('title').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/desserts/sort_desserts_by_title_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_desserts_by_likes_desc(request):
    recipes = Recipe.objects.filter(dish_type='DS').annotate(likes_amount=Count('likes')).order_by(
        F('likes_amount').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/desserts/sort_desserts_by_likes_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_desserts_by_likes_asc(request):
    recipes = Recipe.objects.filter(dish_type='DS').annotate(likes_amount=Count('likes')).order_by(
        F('likes_amount').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/desserts/sort_desserts_by_likes_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

# напитки

def sort_beverages_by_pub_date_desc(request):
    recipes = Recipe.objects.filter(dish_type='BV').order_by(F('publication_date').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/beverages/sort_beverages_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_beverages_by_pub_date_asc(request):
    recipes = Recipe.objects.filter(dish_type='BV').order_by(F('publication_date').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/beverages/sort_beverages_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_beverages_by_title_desc(request):
    recipes = Recipe.objects.filter(dish_type='BV').order_by(F('title').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/beverages/sort_beverages_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_beverages_by_title_asc(request):
    recipes = Recipe.objects.filter(dish_type='BV').order_by(F('title').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/beverages/sort_beverages_by_title_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_beverages_by_likes_desc(request):
    recipes = Recipe.objects.filter(dish_type='BV').annotate(likes_amount=Count('likes')).order_by(
        F('likes_amount').desc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/beverages/sort_beverages_by_likes_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_beverages_by_likes_asc(request):
    recipes = Recipe.objects.filter(dish_type='BV').annotate(likes_amount=Count('likes')).order_by(
        F('likes_amount').asc())
    for recipe in recipes:
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.is_liked = True
        else:
            recipe.is_liked = False
        if recipe.favs.filter(id=request.user.id).exists():
            recipe.is_faved = True
        else:
            recipe.is_faved = False
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/beverages/sort_beverages_by_likes_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })
# конец блока сортировки рецептов