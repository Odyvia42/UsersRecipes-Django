from django.shortcuts import render
from recipeblog.utils import get_all_my_recipes, check_likes_faves, get_paginated


def show_my_recipes_all(request):
    """
    Функция-представление для отображения списка всех рецептов, автором которых является текущий пользователь.
    Функция принимает один параметр: запрос, из которого берётся информация о текущем пользователе.
    Если пользователь вошёл на сайт, функция возвращает веб-страницу с шаблоном my_recipes_all.html
    и контекстом,содержащим два набора рецептов:
    - набор рецептов за авторством текущего пользователя с пагинацией (paged_recipes), который отображается
    на веб-странице;
    - набор со всеми рецептами за авторством текущего пользователя без пагинации (my_recipes),
    который нужен для отображения общего количества рецептов за авторством текущего пользователя.
    Если пользователь не вошёл на сайт, функция не обращается к базе данных, а возвращает веб-страницу
    с шаблоном my_recipes_all.html и пустым контекстом.
    """
    if request.user.is_authenticated:
        my_recipes = get_all_my_recipes(request)
        check_likes_faves(request, my_recipes)
        paged_recipes = get_paginated(request, my_recipes)
        return render(request, 'my-recipes/my_recipes_all.html',
                      {'paged_recipes': paged_recipes,
                       'my_recipes': my_recipes})
    else:
        return render(request, 'my-recipes/my_recipes_all.html')


def show_my_recipes_salads(request):
    """
    Функция-представление для отображения списка всех рецептов в категории "салаты",
    автором которых является текущий пользователь.
    Функция принимает один параметр: запрос, из которого берётся информация о текущем пользователе.
    Если пользователь вошёл на сайт, функция возвращает веб-страницу с шаблоном my_recipes_salads.html
    и контекстом,содержащим два набора рецептов:
    - набор рецептов за авторством текущего пользователя в категории "салаты" с пагинацией (paged_recipes),
    который отображается на веб-странице;
    - набор со всеми рецептами за авторством текущего пользователя в категории "салаты" без пагинации (my_recipes),
    который нужен для отображения общего количества рецептов за авторством текущего пользователя в категории "салаты".
    Если пользователь не вошёл на сайт, функция не обращается к базе данных, а возвращает веб-страницу
    с шаблоном my_recipes_salads.html и пустым контекстом.
    """
    if request.user.is_authenticated:
        my_recipes = get_all_my_recipes(request).filter(dish_type='SL')
        check_likes_faves(request, my_recipes)
        paged_recipes = get_paginated(request, my_recipes)
        return render(request, 'my-recipes/my_recipes_salads.html',
                      {'paged_recipes': paged_recipes,
                       'my_recipes': my_recipes})
    else:
        return render(request, 'my-recipes/my_recipes_salads.html')


def show_my_recipes_first_course(request):
    """
    Функция-представление для отображения списка всех рецептов в категории "первое блюдо",
    автором которых является текущий пользователь.
    Функция принимает один параметр: запрос, из которого берётся информация о текущем пользователе.
    Если пользователь вошёл на сайт, функция возвращает веб-страницу с шаблоном my_recipes_first_course.html
    и контекстом,содержащим два набора рецептов:
    - набор рецептов за авторством текущего пользователя в категории "первое блюдо" с пагинацией (paged_recipes),
    который отображается на веб-странице;
    - набор со всеми рецептами за авторством текущего пользователя в категории "первое блюдо"
    без пагинации (my_recipes), который нужен для отображения общего количества рецептов за авторством
    текущего пользователя в категории "первое блюдо".
    Если пользователь не вошёл на сайт, функция не обращается к базе данных, а возвращает веб-страницу
    с шаблоном my_recipes_first_course.html и пустым контекстом.
    """
    if request.user.is_authenticated:
        my_recipes = get_all_my_recipes(request).filter(dish_type='FC')
        check_likes_faves(request, my_recipes)
        paged_recipes = get_paginated(request, my_recipes)
        return render(request, 'my-recipes/my_recipes_first_course.html',
                      {'paged_recipes': paged_recipes,
                       'my_recipes': my_recipes})
    else:
        return render(request, 'my-recipes/my_recipes_first_course.html')


def show_my_recipes_main_course(request):
    """
    Функция-представление для отображения списка всех рецептов в категории "второе блюдо",
    автором которых является текущий пользователь.
    Функция принимает один параметр: запрос, из которого берётся информация о текущем пользователе.
    Если пользователь вошёл на сайт, функция возвращает веб-страницу с шаблоном my_recipes_main_course.html
    и контекстом,содержащим два набора рецептов:
    - набор рецептов за авторством текущего пользователя в категории "второе блюдо" с пагинацией (paged_recipes),
    который отображается на веб-странице;
    - набор со всеми рецептами за авторством текущего пользователя в категории "второе блюдо"
    без пагинации (my_recipes), который нужен для отображения общего количества рецептов за авторством
    текущего пользователя в категории "второе блюдо".
    Если пользователь не вошёл на сайт, функция не обращается к базе данных, а возвращает веб-страницу
    с шаблоном my_recipes_main_course.html и пустым контекстом.
    """
    if request.user.is_authenticated:
        my_recipes = get_all_my_recipes(request).filter(dish_type='MC')
        check_likes_faves(request, my_recipes)
        paged_recipes = get_paginated(request, my_recipes)
        return render(request, 'my-recipes/my_recipes_main_course.html',
                      {'paged_recipes': paged_recipes,
                       'my_recipes': my_recipes})
    else:
        return render(request, 'my-recipes/my_recipes_main_course.html')


def show_my_recipes_dessert(request):
    """
    Функция-представление для отображения списка всех рецептов в категории "десерт",
    автором которых является текущий пользователь.
    Функция принимает один параметр: запрос, из которого берётся информация о текущем пользователе.
    Если пользователь вошёл на сайт, функция возвращает веб-страницу с шаблоном my_recipes_dessert.html
    и контекстом,содержащим два набора рецептов:
    - набор рецептов за авторством текущего пользователя в категории "десерт" с пагинацией (paged_recipes),
    который отображается на веб-странице;
    - набор со всеми рецептами за авторством текущего пользователя в категории "десерт"
    без пагинации (my_recipes), который нужен для отображения общего количества рецептов за авторством
    текущего пользователя в категории "десерт".
    Если пользователь не вошёл на сайт, функция не обращается к базе данных, а возвращает веб-страницу
    с шаблоном my_recipes_dessert.html и пустым контекстом.
    """
    if request.user.is_authenticated:
        my_recipes = get_all_my_recipes(request).filter(dish_type='DS')
        check_likes_faves(request, my_recipes)
        paged_recipes = get_paginated(request, my_recipes)
        return render(request, 'my-recipes/my_recipes_dessert.html',
                      {'paged_recipes': paged_recipes,
                       'my_recipes': my_recipes})
    else:
        return render(request, 'my-recipes/my_recipes_dessert.html')


def show_my_recipes_bakery(request):
    """
    Функция-представление для отображения списка всех рецептов в категории "выпечка",
    автором которых является текущий пользователь.
    Функция принимает один параметр: запрос, из которого берётся информация о текущем пользователе.
    Если пользователь вошёл на сайт, функция возвращает веб-страницу с шаблоном my_recipes_bakery.html
    и контекстом,содержащим два набора рецептов:
    - набор рецептов за авторством текущего пользователя в категории "выпечка" с пагинацией (paged_recipes),
    который отображается на веб-странице;
    - набор со всеми рецептами за авторством текущего пользователя в категории "выпечка"
    без пагинации (my_recipes), который нужен для отображения общего количества рецептов за авторством
    текущего пользователя в категории "выпечка".
    Если пользователь не вошёл на сайт, функция не обращается к базе данных, а возвращает веб-страницу
    с шаблоном my_recipes_bakery.html и пустым контекстом.
    """
    if request.user.is_authenticated:
        my_recipes = get_all_my_recipes(request).filter(dish_type='BK')
        check_likes_faves(request, my_recipes)
        paged_recipes = get_paginated(request, my_recipes)
        return render(request, 'my-recipes/my_recipes_bakery.html',
                      {'paged_recipes': paged_recipes,
                       'my_recipes': my_recipes})
    else:
        return render(request, 'my-recipes/my_recipes_bakery.html')


def show_my_recipes_beverages(request):
    """
    Функция-представление для отображения списка всех рецептов в категории "напитки",
    автором которых является текущий пользователь.
    Функция принимает один параметр: запрос, из которого берётся информация о текущем пользователе.
    Если пользователь вошёл на сайт, функция возвращает веб-страницу с шаблоном my_recipes_beverages.html
    и контекстом,содержащим два набора рецептов:
    - набор рецептов за авторством текущего пользователя в категории "напитки" с пагинацией (paged_recipes),
    который отображается на веб-странице;
    - набор со всеми рецептами за авторством текущего пользователя в категории "напитки"
    без пагинации (my_recipes), который нужен для отображения общего количества рецептов за авторством
    текущего пользователя в категории "напитки".
    Если пользователь не вошёл на сайт, функция не обращается к базе данных, а возвращает веб-страницу
    с шаблоном my_recipes_beverages.html и пустым контекстом.
    """
    if request.user.is_authenticated:
        my_recipes = get_all_my_recipes(request).filter(dish_type='BV')
        check_likes_faves(request, my_recipes)
        paged_recipes = get_paginated(request, my_recipes)
        return render(request, 'my-recipes/my_recipes_beverages.html',
                      {'paged_recipes': paged_recipes,
                       'my_recipes': my_recipes})
    else:
        return render(request, 'my-recipes/my_recipes_beverages.html')
