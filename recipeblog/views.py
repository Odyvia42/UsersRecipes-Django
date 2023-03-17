from django.contrib.auth import authenticate
from django.core.paginator import Paginator
from django.db.models import F, Count
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, request, HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm

from recipeblog.forms import RegisterUserForm, RecipeForm
from recipeblog.models import User, Recipe




# Create your views here.

def index(request: HttpRequest):
    return render(request, 'index.html')

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'user-detail.html'

class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipe_list'
    template_name = 'recipe-list.html'

class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipe-detail.html'

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