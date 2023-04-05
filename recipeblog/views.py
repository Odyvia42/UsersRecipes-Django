from django.contrib.auth import authenticate
from django.contrib.auth.views import PasswordChangeView
from django.core.paginator import Paginator
from django.db.models import F, Count
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, request, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from recipeblog.forms import RegisterUserForm, RecipeForm, UserForm
from recipeblog.models import User, Recipe




# Create your views here.

def index(request: HttpRequest):
    top_recipes = Recipe.objects.annotate(likes_amount=Count('likes')).order_by(F('likes_amount').desc())[:5]
    return render(request, 'index.html', {'top_recipes': top_recipes})

def show_recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    is_faved = False
    is_liked = False
    if recipe.favs.filter(id=request.user.id).exists():
        is_faved=True
    if recipe.likes.filter(id=request.user.id).exists():
        is_liked=True
    return render(request, 'recipe-detail.html',
                  {'recipe': recipe,
                   'is_faved': is_faved,
                   'is_liked': is_liked,
                   })

class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('password-success')

def change_password_success(request):
    return render(request, 'registration/change-password-success.html', {})

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            return redirect('login')
    else:
        form = RegisterUserForm
    return render(request, 'registration/register_user.html', {'form': form})

def show_user_profile(request, pk):
    user = User.objects.annotate(num_recipes=Count('recipe')).annotate(likes_amount=Count('recipe__likes')).get(pk=pk)
    fav_recipes = user.recipe_favs.all()
    user_recipes = Recipe.objects.filter(author=user)
    return render(request, 'user-detail.html',
                  {'user': user,
                   'fav_recipes': fav_recipes,
                   'user_recipes': user_recipes})


def show_current_user_profile(request, pk):
    current_user = User.objects.annotate(num_recipes=Count('recipe')).annotate(likes_amount=Count('recipe__likes')).filter(id = pk).get()
    my_recipes = Recipe.objects.filter(id = current_user.id)
    return render(request, 'my-profile.html', {'current_user': current_user,
                                               'my_recipes': my_recipes})

# представления для сортировки списка пользователей
def sort_user_list_by_reg_date_asc(request):
    users = User.objects.annotate(num_recipes=Count('recipe')).annotate(likes_amount=Count('recipe__likes')).order_by(F('registration_date').asc())
    p = Paginator(users, 5)
    page = request.GET.get('page')
    paged_users = p.get_page(page)
    return render(request, 'user-list/user-list-sort-by-reg-date-asc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_reg_date_desc(request):
    users = User.objects.annotate(num_recipes=Count('recipe')).annotate(likes_amount=Count('recipe__likes')).order_by(F('registration_date').desc())
    p = Paginator(users, 5)
    page = request.GET.get('page')
    paged_users = p.get_page(page)
    return render(request, 'user-list/user-list-sort-by-reg-date-desc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_username_asc(request):
    users = User.objects.annotate(num_recipes=Count('recipe')).annotate(likes_amount=Count('recipe__likes')).order_by(F('username').asc())
    p = Paginator(users, 5)
    page = request.GET.get('page')
    paged_users = p.get_page(page)
    return render(request, 'user-list/user-list-sort-by-username-asc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_username_desc(request):
    users = User.objects.annotate(num_recipes=Count('recipe')).annotate(likes_amount=Count('recipe__likes')).order_by(F('username').desc())
    users_with_recipes = User.objects.annotate(num_recipes=Count('recipe'))
    p = Paginator(users, 5)
    page = request.GET.get('page')
    paged_users = p.get_page(page)
    return render(request, 'user-list/user-list-sort-by-username-desc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_recipes_amount_asc(request):
    users = User.objects.annotate(num_recipes=Count('recipe')).annotate(likes_amount=Count('recipe__likes')).order_by(F('num_recipes').asc())
    p = Paginator(users, 5)
    page = request.GET.get('page')
    paged_users = p.get_page(page)
    return render(request, 'user-list/user-list-sort-by-recipes-amount-asc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_recipes_amount_desc(request):
    users = User.objects.annotate(num_recipes=Count('recipe')).annotate(likes_amount=Count('recipe__likes')).order_by(F('num_recipes').desc())
    p = Paginator(users, 5)
    page = request.GET.get('page')
    paged_users = p.get_page(page)
    return render(request, 'user-list/user-list-sort-by-recipes-amount-desc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_rating_asc(request):
    users = User.objects.annotate(num_recipes=Count('recipe')).annotate(likes_amount=Count('recipe__likes')).order_by(F('likes_amount').asc())
    p = Paginator(users, 5)
    page = request.GET.get('page')
    paged_users = p.get_page(page)
    return render(request, 'user-list/user-list-sort-by-rating-asc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_rating_desc(request):
    users = User.objects.annotate(num_recipes=Count('recipe')).annotate(likes_amount=Count('recipe__likes')).order_by(F('likes_amount').desc())
    p = Paginator(users, 5)
    page = request.GET.get('page')
    paged_users = p.get_page(page)
    return render(request, 'user-list/user-list-sort-by-rating-desc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

# представления для форм создания и обновления рецептов
def add_recipe(request):
    submitted = False
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect('/add-recipe?submitted=True')
    else:
        form = RecipeForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add-recipe.html',
                  {'form': form,
                   'submitted': submitted})

def update_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    form = RecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('recipe-detail', pk=recipe_id)
    return render(request, 'update-recipe.html',
                  {'recipe': recipe,
                   'form': form})

def update_user(request, user_id):
    user = User.objects.get(pk=user_id)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('my-profile', pk=user_id)
    return render(request, 'update-user.html',
                  {'user': user,
                   'form': form})

# представления для сортировки списка рецептов, основная категоризация по типу блюда

# все рецепты
def sort_all_recipes_by_pub_date_desc(request):
    recipes = Recipe.objects.order_by(F('publication_date').desc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })
def sort_all_recipes_by_pub_date_asc(request):
    recipes = Recipe.objects.order_by(F('publication_date').asc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_all_recipes_by_title_desc(request):
    recipes = Recipe.objects.order_by(F('title').desc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })
def sort_all_recipes_by_title_asc(request):
    recipes = Recipe.objects.order_by(F('title').asc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_title_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_all_recipes_by_likes_desc(request):
    recipes = Recipe.objects.annotate(likes_amount=Count('likes')).order_by(F('likes_amount').desc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_likes_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })
def sort_all_recipes_by_likes_asc(request):
    recipes = Recipe.objects.annotate(likes_amount=Count('likes')).order_by(F('likes_amount').asc())
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
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/salads/sort_salads_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_salads_by_pub_date_asc(request):
    recipes = Recipe.objects.filter(dish_type='SL').order_by(F('publication_date').asc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/salads/sort_salads_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_salads_by_title_desc(request):
    recipes = Recipe.objects.filter(dish_type='SL').order_by(F('title').desc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/salads/sort_salads_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_salads_by_title_asc(request):
    recipes = Recipe.objects.filter(dish_type='SL').order_by(F('title').asc())
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
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/first-course/sort_first_courses_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_first_courses_by_pub_date_asc(request):
    recipes = Recipe.objects.filter(dish_type='FC').order_by(F('publication_date').asc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/first-course/sort_first_courses_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_first_courses_by_title_desc(request):
    recipes = Recipe.objects.filter(dish_type='FC').order_by(F('title').desc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/first-course/sort_first_courses_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_first_courses_by_title_asc(request):
    recipes = Recipe.objects.filter(dish_type='FC').order_by(F('title').asc())
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
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/main-course/sort_main_courses_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_main_courses_by_pub_date_asc(request):
    recipes = Recipe.objects.filter(dish_type='MC').order_by(F('publication_date').asc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/main-course/sort_main_courses_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_main_courses_by_title_desc(request):
    recipes = Recipe.objects.filter(dish_type='MC').order_by(F('title').desc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/main-course/sort_main_courses_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_main_courses_by_title_asc(request):
    recipes = Recipe.objects.filter(dish_type='MC').order_by(F('title').asc())
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
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/bakery/sort_bakery_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_bakery_by_pub_date_asc(request):
    recipes = Recipe.objects.filter(dish_type='BK').order_by(F('publication_date').asc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/bakery/sort_bakery_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_bakery_by_title_desc(request):
    recipes = Recipe.objects.filter(dish_type='BK').order_by(F('title').desc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/bakery/sort_bakery_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_bakery_by_title_asc(request):
    recipes = Recipe.objects.filter(dish_type='BK').order_by(F('title').asc())
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
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/desserts/sort_desserts_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_desserts_by_pub_date_asc(request):
    recipes = Recipe.objects.filter(dish_type='DS').order_by(F('publication_date').asc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/desserts/sort_desserts_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_desserts_by_title_desc(request):
    recipes = Recipe.objects.filter(dish_type='DS').order_by(F('title').desc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/desserts/sort_desserts_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_desserts_by_title_asc(request):
    recipes = Recipe.objects.filter(dish_type='DS').order_by(F('title').asc())
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
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/beverages/sort_beverages_by_pub_date_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_beverages_by_pub_date_asc(request):
    recipes = Recipe.objects.filter(dish_type='BV').order_by(F('publication_date').asc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/beverages/sort_beverages_by_pub_date_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })


def sort_beverages_by_title_desc(request):
    recipes = Recipe.objects.filter(dish_type='BV').order_by(F('title').desc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/beverages/sort_beverages_by_title_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })

def sort_beverages_by_title_asc(request):
    recipes = Recipe.objects.filter(dish_type='BV').order_by(F('title').asc())
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
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/beverages/sort_beverages_by_likes_asc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })
# конец блока сортировки рецептов

def like_recipe(request, pk):
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
    else:
        recipe.likes.add(request.user)
    return HttpResponseRedirect(reverse('recipe-detail', args=[str(pk)]))

def fave_recipe(request, pk):
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    if recipe.favs.filter(id=request.user.id).exists():
        recipe.favs.remove(request.user)
    else:
        recipe.favs.add(request.user)
    return HttpResponseRedirect(reverse('recipe-detail', args=[str(pk)]))

# Блок "Избранное" текущего пользователя

def show_my_favs_all(request):
    user = request.user
    fav_recipes = user.recipe_favs.all()
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-favs/my_favs_all.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes})

def show_my_favs_salads(request):
    user = request.user
    fav_recipes = user.recipe_favs.filter(dish_type='SL')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-favs/my_favs_salads.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes})

def show_my_favs_first_course(request):
    user = request.user
    fav_recipes = user.recipe_favs.filter(dish_type='FC')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-favs/my_favs_first_course.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes})

def show_my_favs_main_course(request):
    user = request.user
    fav_recipes = user.recipe_favs.filter(dish_type='MC')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-favs/my_favs_main_course.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes})

def show_my_favs_dessert(request):
    user = request.user
    fav_recipes = user.recipe_favs.filter(dish_type='DS')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-favs/my_favs_dessert.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes})

def show_my_favs_bakery(request):
    user = request.user
    fav_recipes = user.recipe_favs.filter(dish_type='BK')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-favs/my_favs_bakery.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes})

def show_my_favs_beverages(request):
    user = request.user
    fav_recipes = user.recipe_favs.filter(dish_type='BV')
    p = Paginator(fav_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'my-favs/my_favs_beverages.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes})

# Блок "Мои рецепты"
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


# Блок "Избранное" для любого пользователя
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


# Блок показа всех рецептов конкретного пользователя

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