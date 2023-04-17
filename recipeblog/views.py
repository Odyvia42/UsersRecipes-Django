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
from taggit.models import Tag

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
    user = User.objects.annotate(num_recipes=Count('recipe', distinct=True)).annotate(likes_amount=Count('recipe__likes')).get(pk=pk)
    fav_recipes = user.recipe_favs.all()
    user_recipes = Recipe.objects.filter(author=user)
    return render(request, 'user-detail.html',
                  {'user': user,
                   'fav_recipes': fav_recipes,
                   'user_recipes': user_recipes})


def show_current_user_profile(request, pk):
    current_user = User.objects.annotate(num_recipes=Count('recipe', distinct=True)).annotate(likes_amount=Count('recipe__likes')).filter(id = pk).get()
    my_recipes = Recipe.objects.filter(id = current_user.id)
    return render(request, 'my-profile.html', {'current_user': current_user,
                                               'my_recipes': my_recipes})



# представления для форм создания и обновления рецептов
def add_recipe(request):
    submitted = False
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            form.save_m2m()
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
        form.save_m2m()
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

# Получение списка рецептов по тегу
def show_recipes_by_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    tagged_recipes = Recipe.objects.filter(tags=tag)
    p = Paginator(tagged_recipes, 5)
    page = request.GET.get('page')
    paged_recipes = p.get_page(page)
    return render(request, 'recipes_by_tag.html',
                  {'paged_recipes': paged_recipes,
                   'tag': tag})

def show_all_tags(request):
    tags = Tag.objects.all().annotate(num_recipes=Count('taggit_taggeditem_items')).order_by(F('name'))
    top_tags = Recipe.tags.most_common().annotate(num_recipes=Count('taggit_taggeditem_items'))[:5]
    return render(request, 'all_tags.html',
                  {'tags': tags,
                   'top_tags': top_tags})

def show_all_authors(request):
    authors = User.objects.annotate(num_recipes=Count('recipe')).order_by(F('username').asc())
    return render(request, 'all_authors.html',
                  {'authors': authors,
                   })
