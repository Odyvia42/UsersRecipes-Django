from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.db.models import F, Count
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from taggit.models import Tag
from recipeblog.forms import RegisterUserForm, RecipeForm, UserForm
from recipeblog.models import User, Recipe
from recipeblog.utils import check_likes_faves, get_paginated, get_all_users, order_by_likes_amount_desc


# Create your views here.


def index(request: HttpRequest):
    """
    Функция-представление для отображения главной страницы сайта с пятью лучшими по рейтингу рецептами.
    Функция принимает один параметр - запрос.
    Функция получает из базы данных список всех рецептов, отсортированный по количеству лайков в них
    (по убыванию), после чего выбирает первые пять из них и для каждого рецепта актуализирует состояние
    лайка/избранного (лайкнут ли пост/добавлен ли в избранное текущим пользователем).
    Функция возвращает веб-страницу с шаблоном index.html и контекстом, в который передан набор
    из пяти лучших по рейтингу рецептов.
    """
    top_recipes = order_by_likes_amount_desc(Recipe.objects.all())[:5]
    check_likes_faves(request, top_recipes)
    return render(request, 'index.html', {'top_recipes': top_recipes})


def show_recipe_detail(request, pk):
    """
    Функция-представление для отображения страницы с деталями рецепта.
    Функция принимает два параметра:
    :param request: запрос, из которого берётся информация о текущем пользователе;
    :param pk: идентификатор (id) рецепта.
    Функция получает из базы данных рецепт по переданному id, после чего актуализирует состояние
    лайка/избранного (лайкнут ли рецепт/добавлен ли в избранное текущим пользователем).
    Функция возвращает веб-страницу с шаблоном recipe-detail.html и контекстом, в который передан запрошенный рецепт.
    """
    recipe = Recipe.objects.get(pk=pk)
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.is_liked = True
    else:
        recipe.is_liked = False
    if recipe.favs.filter(id=request.user.id).exists():
        recipe.is_faved = True
    else:
        recipe.is_faved = False
    return render(request, 'recipe-detail.html',
                  {'recipe': recipe})


class ChangePasswordView(PasswordChangeView, LoginRequiredMixin):
    """
    Класс-представление для отображения формы смены пароля.
    Отображает форму PasswordChangeForm на веб-странице с шаблоном change-password.html.
    При успешной смене пароля перенаправляет на страницу с сообщением об успешной смене пароля.
    """
    form_class = PasswordChangeForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('password-success')


def change_password_success(request):
    """
    Функция-представление для отображения страницы с сообщением об успешной смене пароля.
    Функция принимает один параметр: запрос.
    Функция возвращает веб-страницу с шаблоном change-password-success.html и пустым контекстом.
    """
    return render(request, 'registration/change-password-success.html', {})


def register_user(request):
    """
    Функция-представление для регистрации нового пользователя.
    Функция получает один параметр: запрос.
    Функция возвращает веб-страницу с шаблоном register_user.html и контекстом, содержащим
    форму для регистрации нового пользователя.
    Если метод запроса - POST, то функция отображает форму для регистрации пользователя.
    Если форма заполнена верно и прошла валидацию, информация о новом пользователе сохраняется в базе данных,
    а функция перенапраправляет на страницу входа на сайт.
    В противном случае функция вновь отображает форму для регистрации пользователя.
    """
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
    """
    Функция-представление для отображения профиля пользователя, отличного от текущего пользователя.
    Функция принимает два параметра:
    :param request: запрос;
    :param pk: идентификатор (id) пользователя, профиль которого нужно отобразить.
    Функция получает из базы данных информацию о пользователе с переданным id, а также набор избранных
    рецептов данного пользователя (fav_recipes) и набор рецептов за авторством данного пользователя
    (user_recipes).
    Функция возвращает веб-страницу с шаблоном user-detail.html и контекстом, содержащим словарь user
    с информацией о выбранном пользователе, а также два набора рецептов (fav_recipes и user_recipes),
    которые нужны для отображения количества избранных рецептов данного пользователя и рецептов за авторством
    данного пользователя соответственно.
    """
    user = get_all_users().get(pk=pk)
    fav_recipes = user.recipe_favs.all()
    user_recipes = Recipe.objects.filter(author=user)
    return render(request, 'user-detail.html',
                  {'user': user,
                   'fav_recipes': fav_recipes,
                   'user_recipes': user_recipes})


def show_current_user_profile(request, pk):
    """
    Функция-представление для отображения профиля текущего пользователя.
    Функция принимает два параметра:
    :param request: запрос, из которого берётся информация о текущем пользователе;
    :param pk: идентификатор (id) текущего пользователя.
    Функция получает из базы данных информацию о текущем пользователе, а также набор рецептов за авторством
    текущего пользователя (my_recipes).
    Функция возвращает веб-страницу с шаблоном my-profile.html и контекстом, содержащим словарь current_user
    с информацией о текущем пользователе, а также набор рецептов my_recipes, который нужен для отображения
    количества рецептов за авторством текущего пользователя.
    """
    current_user = get_all_users().get(id=pk)
    my_recipes = Recipe.objects.filter(id=current_user.id)
    return render(request, 'my-profile.html', {'current_user': current_user,
                                               'my_recipes': my_recipes})


# представления для форм создания и обновления рецептов
def add_recipe(request):
    """
    Функция-представление для добавления нового рецепта.
    Функция принимает один параметр: запрос, из которого берётся информация о текущем пользователе.
    Функция возвращает веб-страницу с шаблоном add-recipe.html и контекстом, содержащим форму для
    нового рецепта и параметр submitted.
    По умолчанию функция устанавливает для страницы параметр submitted = False. Это значит, что форма
    ещё не была передана для сохранения.
    Если метод запроса - POST, функция отображает форму добавления рецепта.
    Если форма заполнена верно и прошла валидацию, функция приостанавливает сохранение формы
    параметром commit=False, добавляет к новому рецепту автора - текущего пользователя, после чего
    сохраняет форму и перенаправляет на эту же страницу, но передавая параметр submitted=True.
    В противном случае функция отображает ту же самую форму.
    Если в запросе содержится параметр submitted=True, функция устанавливает этот параметр на True.
    Это значит, что форма была передана для сохранения.
    """
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
    """
    Функция-представление для редактирования выбранного рецепта.
    Функция принимает два параметра:
    :param request: запрос, из которого берётся информация о текущем пользователе;
    :param recipe_id: идентификатор (id) рецепта, который нужно отредактировать.
    Функция возвращает веб-страницу с шаблоном update-recipe.html и контекстом, содержащим рецепт,
    который нужно отредактировать, и форму для редактирования рецепта.
    Функция получает из базы данных рецепт по переданному id, после чего отображает форму редактирования
    рецепта, при этом предзаполняя поля данными из полученного по id рецепта.
    Если форма заполнена верно и прошла валидацию, функция сохраняет новые данные в базе данных и
    перенаправляет на страницу с деталями данного рецепта.

    """
    recipe = Recipe.objects.get(pk=recipe_id)
    form = RecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form.save_m2m()
        return redirect('recipe-detail', pk=recipe_id)
    return render(request, 'update-recipe.html',
                  {'recipe': recipe,
                   'form': form})


def update_user(request, user_id):
    """
    Функция-представление для редактирования данных текущего пользователя.
    Функция принимает два параметра:
    :param request: запрос;
    :param user_id: идентификатор (id) текущего пользователя.
    Функция возвращает веб-страницу с шаблоном update-user.html и контекстом, содержащим словарь с
    информацией о текущем пользователе и форму для редактирования профиля пользователя.
    Функция получает из базы данных информацию о текущем пользователе по его id, после чего отображает
    форму для редактирования профиля пользователя, предзаполняя её данными, полученными из базы данных.
    Если форма заполнена верно и прошла валидацию, функция сохраняет новые значения в базе данных и
    перенаправляет на страницу профиля текущего пользователя.
    """
    user = User.objects.get(pk=user_id)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('my-profile', pk=user_id)
    return render(request, 'update-user.html',
                  {'user': user,
                   'form': form})


def like_recipe(request, pk):  # убрать неиспользуемый pk
    """
    Функция-представление для простановки лайка рецепту/удаления лайка с рецепта.
    Функция принимает один параметр: запрос, из которого берётся информация о текущем пользователе и
    рецепте.
    Функция получает из базы данных информацию о рецепте по идентификатору (id) рецепта, после чего проверяет,
    лайкнул ли уже текущий пользователь данный рецепт, или ещё нет.
    Если текущий пользователь уже поставил лайк рецепту, функция убирает этот лайк, в противном случае - добавляет.
    Функция возвращает перенаправление на ту же самую страницу, где текущий пользователь нажал кнопку лайка.
    """
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
    else:
        recipe.likes.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def fave_recipe(request, pk):  # убрать неиспользуемый pk
    """
    Функция-представление для добавления рецепта в избранное/удаления рецепта из избранного.
    Функция принимает один параметр: запрос, из которого берётся информация о текущем пользователе и
    рецепте.
    Функция получает из базы данных информацию о рецепте по идентификатору (id) рецепта, после чего проверяет,
    добавил ли уже текущий пользователь данный рецепт в избранное, или ещё нет.
    Если текущий пользователь уже добавил данный рецепт в избранное, функция убирает этот рецепт из избранного,
    в противном случае - добавляет.
    Функция возвращает перенаправление на ту же самую страницу, где текущий пользователь нажал кнопку
    "добавить в избранное"/"удалить из избранного".
    """
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    if recipe.favs.filter(id=request.user.id).exists():
        recipe.favs.remove(request.user)
    else:
        recipe.favs.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Получение списка рецептов по тегу
def show_recipes_by_tag(request, slug):
    """
    Функция-представление для получения списка рецептов по конкретному тегу.
    Функция получает два параметра:
    :param request: запрос, из которого берётся информация о текущем пользователе;
    :param slug: текст запрошенного тега.
    Функция получает из базы данных тег, соответствующий запрошенному, после чего получает список всех
    рецептов, в которых используется этот тег, для каждого рецепта актуализирует состояние лайка/избранного
    (лайкнут ли пост/добавлен ли в избранное текущим пользователем), после чего добавляет к набору рецептов
    пагинацию.
    Функция возвращает веб-страницу с шаблоном recipes_by_tag.html и контекстом, содержащим набор рецептов
    с пагинацией (paged_recipes), а также переданный тег.
    """
    tag = get_object_or_404(Tag, slug=slug)
    tagged_recipes = Recipe.objects.filter(tags=tag)
    check_likes_faves(request, tagged_recipes)
    paged_recipes = get_paginated(request, tagged_recipes)
    return render(request, 'recipes_by_tag.html',
                  {'paged_recipes': paged_recipes,
                   'tag': tag})


def show_all_tags(request):
    """
    Функция для отображения списка всех сохранённых тегов, по которым на сайте есть опубликованные рецепты.
    Функция получает один параметр: запрос.
    Функция получает из базы данных набор всех сохранённых тегов, аннотируя каждый по количеству рецептов,
    которые его используют, и сортируя полученный набор в прямом алфавитном порядке.
    Отдельным запросом функция также получает набор из 5 тегов, которые используются в наибольшем количестве
    рецептов, аннотируя каждый по количеству рецептов и сортируя по убыванию.
    Функция возвращает веб-страницу с шаблоном all_tags.html и двумя наборами тегов: всеми используемыми
    тегами, отсортированными в прямом алфавитном порядке (all_tags), и пятью самыми популярными (по количеству
    рецептов) тегами, отсортированными по убыванию количества рецептов (top_tags).
    """
    tags = Tag.objects.all().annotate(num_recipes=Count('taggit_taggeditem_items')).order_by(F('name'))
    top_tags = Recipe.tags.most_common().annotate(num_recipes=Count('taggit_taggeditem_items'))[:5]
    return render(request, 'all_tags.html',
                  {'tags': tags,
                   'top_tags': top_tags})


def show_all_authors(request):
    """
    Функция-представление для отображения списка пользователей, у которых есть хотя бы один опубликованный рецепт.
    Функция получает один параметр: запрос.
    Функция получает из базы данных набор всех пользователей сайта, аннотируя каждого по количеству рецептов
    за авторством этого пользователя и сортируя пользователей в прямом алфавитном порядке.
    Функция возвращает веб-страницу с шаблоном all_authors.html и контекстом, содержащим отсортированный
    набор авторов. Проверка на ненулевое количество рецептов (num_recipes > 0) происходит внутри шаблона веб-страницы.
    """
    authors = User.objects.annotate(num_recipes=Count('recipe')).order_by(F('username').asc())
    return render(request, 'all_authors.html',
                  {'authors': authors,
                   })
