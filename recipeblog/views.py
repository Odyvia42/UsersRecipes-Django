from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, request
from django.views import generic
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm

from recipeblog.forms import RegisterUserForm
from recipeblog.models import User, Recipe




# Create your views here.

def index(request: HttpRequest):
    return render(request, 'index.html')


class UserListView(ListView):
    model = User
    context_object_name = 'user_list'
    template_name = 'user-list.html'

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
    return render(request, 'my-profile.html', {'my_recipes':my_recipes})




