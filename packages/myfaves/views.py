from django.shortcuts import render
from recipeblog.utils import get_all_my_favs, get_paginated, check_likes_faves


def show_my_favs_all(request):
    """
    Функция-представление для отображения списка всех рецептов, добавленных в избранное текущим пользователем.
    Функция принимает один параметр: запрос, из которого берётся информация о текущем пользователе.
    Если пользователь вошёл на сайт, функция получает из базы данных набор рецептов, добавленных в избранное
    текущим пользователем, для каждого рецепта актуализирует состояние лайка/избранного (лайкнут ли пост/добавлен
    ли в избранное текущим пользователем), а также добавляет к набору рецептов пагинацию.
    Функция возвращает веб-страницу с шаблоном my_favs_all.html и контекстом, содержащим два набора рецептов:
    - набор избранных рецептов с пагинацией (paged_recipes), который отображается на веб-странице;
    - набор со всеми избранными рецептами без пагинации (fav_recipes), который нужен для отображения
    общего количества избранных рецептов.
    Если пользователь не вошёл на сайт, функция не обращается к базе данных, а возвращает веб-страницу
    с шаблоном my_favs_all.html и пустым контекстом.
    """
    if request.user.is_authenticated:
        fav_recipes = get_all_my_favs(request)
        check_likes_faves(request, fav_recipes)
        paged_recipes = get_paginated(request, fav_recipes)
        return render(request, 'my-favs/my_favs_all.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_all.html')


def show_my_favs_salads(request):
    """
    Функция-представление для отображения списка всех рецептов в категории "салаты",
    добавленных в избранное текущим пользователем.
    Функция принимает один параметр: запрос, из которого берётся информация о текущем пользователе.
    Если пользователь вошёл на сайт, функция получает из базы данных набор рецептов в категории "салаты",
    добавленных в избранное текущим пользователем, для каждого рецепта актуализирует состояние лайка/избранного
    (лайкнут ли пост/добавлен ли в избранное текущим пользователем), а также добавляет к набору рецептов пагинацию.
    Функция возвращает веб-страницу с шаблоном my_favs_salads.html и контекстом, содержащим два набора рецептов:
    - набор избранных рецептов в категории "салаты" с пагинацией (paged_recipes), который отображается
    на веб-странице;
    - набор со всеми избранными рецептами в категории "салаты" без пагинации (fav_recipes), который нужен
    для отображения общего количества избранных рецептов в категории "салаты".
    Если пользователь не вошёл на сайт, функция не обращается к базе данных, а возвращает веб-страницу
    с шаблоном my_favs_salads.html и пустым контекстом.
    """
    if request.user.is_authenticated:
        fav_recipes = get_all_my_favs(request).filter(dish_type='SL')
        check_likes_faves(request, fav_recipes)
        paged_recipes = get_paginated(request, fav_recipes)
        return render(request, 'my-favs/my_favs_salads.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_salads.html')


def show_my_favs_first_course(request):
    """
    Функция-представление для отображения списка всех рецептов в категории "первое блюдо",
    добавленных в избранное текущим пользователем.
    Функция принимает один параметр: запрос, из которого берётся информация о текущем пользователе.
    Если пользователь вошёл на сайт, функция получает из базы данных набор рецептов в категории "первое блюдо",
    добавленных в избранное текущим пользователем, для каждого рецепта актуализирует состояние лайка/избранного
    (лайкнут ли пост/добавлен ли в избранное текущим пользователем), а также добавляет к набору рецептов пагинацию.
    Функция возвращает веб-страницу с шаблоном my_favs_first_course.html и контекстом, содержащим два набора рецептов:
    - набор избранных рецептов в категории "первое блюдо" с пагинацией (paged_recipes), который отображается
    на веб-странице;
    - набор со всеми избранными рецептами в категории "первое блюдо" без пагинации (fav_recipes), который нужен
    для отображения общего количества избранных рецептов в категории "первое блюдо".
    Если пользователь не вошёл на сайт, функция не обращается к базе данных, а возвращает веб-страницу
    с шаблоном my_favs_first_course.html и пустым контекстом.
    """
    if request.user.is_authenticated:
        fav_recipes = get_all_my_favs(request).filter(dish_type='FC')
        check_likes_faves(request, fav_recipes)
        paged_recipes = get_paginated(request, fav_recipes)
        return render(request, 'my-favs/my_favs_first_course.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_first_course.html')


def show_my_favs_main_course(request):
    """
    Функция-представление для отображения списка всех рецептов в категории "второе блюдо",
    добавленных в избранное текущим пользователем.
    Функция принимает один параметр: запрос, из которого берётся информация о текущем пользователе.
    Если пользователь вошёл на сайт, функция получает из базы данных набор рецептов в категории "второе блюдо",
    добавленных в избранное текущим пользователем, для каждого рецепта актуализирует состояние лайка/избранного
    (лайкнут ли пост/добавлен ли в избранное текущим пользователем), а также добавляет к набору рецептов пагинацию.
    Функция возвращает веб-страницу с шаблоном my_favs_main_course.html и контекстом, содержащим два набора рецептов:
    - набор избранных рецептов в категории "второе блюдо" с пагинацией (paged_recipes), который отображается
    на веб-странице;
    - набор со всеми избранными рецептами в категории "второе блюдо" без пагинации (fav_recipes), который нужен
    для отображения общего количества избранных рецептов в категории "второе блюдо".
    Если пользователь не вошёл на сайт, функция не обращается к базе данных, а возвращает веб-страницу
    с шаблоном my_favs_main_course.html и пустым контекстом.
    """
    if request.user.is_authenticated:
        fav_recipes = get_all_my_favs(request).filter(dish_type='MC')
        check_likes_faves(request, fav_recipes)
        paged_recipes = get_paginated(request, fav_recipes)
        return render(request, 'my-favs/my_favs_main_course.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_main_course.html')


def show_my_favs_dessert(request):
    """
    Функция-представление для отображения списка всех рецептов в категории "десерт",
    добавленных в избранное текущим пользователем.
    Функция принимает один параметр: запрос, из которого берётся информация о текущем пользователе.
    Если пользователь вошёл на сайт, функция получает из базы данных набор рецептов в категории "десерт",
    добавленных в избранное текущим пользователем, для каждого рецепта актуализирует состояние лайка/избранного
    (лайкнут ли пост/добавлен ли в избранное текущим пользователем), а также добавляет к набору рецептов пагинацию.
    Функция возвращает веб-страницу с шаблоном my_favs_dessert.html и контекстом, содержащим два набора рецептов:
    - набор избранных рецептов в категории "десерт" с пагинацией (paged_recipes), который отображается
    на веб-странице;
    - набор со всеми избранными рецептами в категории "десерт" без пагинации (fav_recipes), который нужен
    для отображения общего количества избранных рецептов в категории "десерт".
    Если пользователь не вошёл на сайт, функция не обращается к базе данных, а возвращает веб-страницу
    с шаблоном my_favs_dessert.html и пустым контекстом.
    """
    if request.user.is_authenticated:
        fav_recipes = get_all_my_favs(request).filter(dish_type='DS')
        check_likes_faves(request, fav_recipes)
        paged_recipes = get_paginated(request, fav_recipes)
        return render(request, 'my-favs/my_favs_dessert.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_dessert.html')


def show_my_favs_bakery(request):
    """
    Функция-представление для отображения списка всех рецептов в категории "выпечка",
    добавленных в избранное текущим пользователем.
    Функция принимает один параметр: запрос, из которого берётся информация о текущем пользователе.
    Если пользователь вошёл на сайт, функция получает из базы данных набор рецептов в категории "выпечка",
    добавленных в избранное текущим пользователем, для каждого рецепта актуализирует состояние лайка/избранного
    (лайкнут ли пост/добавлен ли в избранное текущим пользователем), а также добавляет к набору рецептов пагинацию.
    Функция возвращает веб-страницу с шаблоном my_favs_bakery.html и контекстом, содержащим два набора рецептов:
    - набор избранных рецептов в категории "выпечка" с пагинацией (paged_recipes), который отображается
    на веб-странице;
    - набор со всеми избранными рецептами в категории "выпечка" без пагинации (fav_recipes), который нужен
    для отображения общего количества избранных рецептов в категории "выпечка".
    Если пользователь не вошёл на сайт, функция не обращается к базе данных, а возвращает веб-страницу
    с шаблоном my_favs_bakery.html и пустым контекстом.
    """
    if request.user.is_authenticated:
        fav_recipes = get_all_my_favs(request).filter(dish_type='BK')
        check_likes_faves(request, fav_recipes)
        paged_recipes = get_paginated(request, fav_recipes)
        return render(request, 'my-favs/my_favs_bakery.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_bakery.html')


def show_my_favs_beverages(request):
    """
    Функция-представление для отображения списка всех рецептов в категории "напитки",
    добавленных в избранное текущим пользователем.
    Функция принимает один параметр: запрос, из которого берётся информация о текущем пользователе.
    Если пользователь вошёл на сайт, функция получает из базы данных набор рецептов в категории "напитки",
    добавленных в избранное текущим пользователем, для каждого рецепта актуализирует состояние лайка/избранного
    (лайкнут ли пост/добавлен ли в избранное текущим пользователем), а также добавляет к набору рецептов пагинацию.
    Функция возвращает веб-страницу с шаблоном my_favs_beverages.html и контекстом, содержащим два набора рецептов:
    - набор избранных рецептов в категории "напитки" с пагинацией (paged_recipes), который отображается
    на веб-странице;
    - набор со всеми избранными рецептами в категории "напитки" без пагинации (fav_recipes), который нужен
    для отображения общего количества избранных рецептов в категории "напитки".
    Если пользователь не вошёл на сайт, функция не обращается к базе данных, а возвращает веб-страницу
    с шаблоном my_favs_beverages.html и пустым контекстом.
    """
    if request.user.is_authenticated:
        fav_recipes = get_all_my_favs(request).filter(dish_type='BV')
        check_likes_faves(request, fav_recipes)
        paged_recipes = get_paginated(request, fav_recipes)
        return render(request, 'my-favs/my_favs_beverages.html',
                      {'paged_recipes': paged_recipes,
                       'fav_recipes': fav_recipes})
    else:
        return render(request, 'my-favs/my_favs_beverages.html')
