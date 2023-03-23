from django.contrib.auth import authenticate
from django.contrib.auth.views import PasswordChangeView
from django.core.paginator import Paginator
from django.db.models import F, Count
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, request, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from recipeblog.forms import RegisterUserForm, RecipeForm, UserForm
from recipeblog.models import User, Recipe




# Create your views here.

def index(request: HttpRequest):
    return render(request, 'index.html')

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'user-detail.html'



class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipe-detail.html'

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

def show_current_user_profile(request, pk):
    current_user = User.objects.filter(id = pk).get()
    my_recipes = Recipe.objects.filter(id = current_user.id)
    return render(request, 'my-profile.html', {'my_recipes': my_recipes})

# представления для сортировки списка пользователей
def sort_user_list_by_reg_date_asc(request):
    users = User.objects.annotate(num_recipes=Count('recipe')).order_by(F('registration_date').asc())
    p = Paginator(users, 5)
    page = request.GET.get('page')
    paged_users = p.get_page(page)
    return render(request, 'user-list/user-list-sort-by-reg-date-asc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_reg_date_desc(request):
    users = User.objects.annotate(num_recipes=Count('recipe')).order_by(F('registration_date').desc())
    p = Paginator(users, 5)
    page = request.GET.get('page')
    paged_users = p.get_page(page)
    return render(request, 'user-list/user-list-sort-by-reg-date-desc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_username_asc(request):
    users = User.objects.annotate(num_recipes=Count('recipe')).order_by(F('username').asc())
    p = Paginator(users, 5)
    page = request.GET.get('page')
    paged_users = p.get_page(page)
    return render(request, 'user-list/user-list-sort-by-username-asc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_username_desc(request):
    users = User.objects.annotate(num_recipes=Count('recipe')).order_by(F('username').desc())
    users_with_recipes = User.objects.annotate(num_recipes=Count('recipe'))
    p = Paginator(users, 5)
    page = request.GET.get('page')
    paged_users = p.get_page(page)
    return render(request, 'user-list/user-list-sort-by-username-desc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_recipes_amount_asc(request):
    users = User.objects.annotate(num_recipes=Count('recipe')).order_by(F('num_recipes').asc())
    p = Paginator(users, 5)
    page = request.GET.get('page')
    paged_users = p.get_page(page)
    return render(request, 'user-list/user-list-sort-by-recipes-amount-asc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_recipes_amount_desc(request):
    users = User.objects.annotate(num_recipes=Count('recipe')).order_by(F('num_recipes').desc())
    p = Paginator(users, 5)
    page = request.GET.get('page')
    paged_users = p.get_page(page)
    return render(request, 'user-list/user-list-sort-by-recipes-amount-desc.html',
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
    recipes = Recipe.objects.order_by(F('likes').desc())
    p = Paginator(recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipe-list/all-recipes/sort_all_recipes_by_likes_desc.html',
                  {'recipes': recipes,
                   'paged_recipes': paged_recipes,
                   })
def sort_all_recipes_by_likes_asc(request):
    recipes = Recipe.objects.order_by(F('likes').asc())
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