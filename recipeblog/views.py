from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView

from recipeblog.models import User, Recipe


# Create your views here.

def index(request: HttpRequest):
    return render(request, 'index.html')


class UserListView(ListView):
    model = User
    context_object_name = 'user_list'
    template_name = 'user-list.html'

class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipe_list'
    template_name = 'recipe-list.html'



