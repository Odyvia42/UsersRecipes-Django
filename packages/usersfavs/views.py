from django.shortcuts import render
from recipeblog.utils import *


def show_user_favs_all(request, pk):
    """
    Функция-представление для отображения списка всех рецептов, добавленных в избранное любым пользователем сайта,
    отличным от текущего пользователя.
    Функция принимает два параметра:
    :param request - запрос, из которого берётся информация о текущем пользователе;
    :param pk - идентификатор пользователя, чьи избранные рецепты надо отобразить.
    Функция получает из базы данных набор рецептов, добавленных в избранное пользователем, чей идентификатор
    был передан функции, для каждого рецепта актуализирует состояние лайка/избранного (лайкнут ли пост/добавлен
    ли в избранное текущим пользователем), а также добавляет к набору рецептов пагинацию.
    Функция возвращает веб-страницу с шаблоном user_favs.html и контекстом, содержащим два набора рецептов:
    - набор избранных рецептов с пагинацией (paged_recipes), который отображается на веб-странице;
    - набор со всеми избранными рецептами без пагинации (fav_recipes), который нужен для отображения
    общего количества избранных рецептов;
    а также словарь 'user' с информацией о запрошенном пользователе
    (для отображения никнейма запрошенного пользователя).
    """
    user = get_user_by_id(pk)
    fav_recipes = get_all_users_favs(pk)
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})


def show_user_favs_salads(request, pk):
    """
    Функция-представление для отображения списка всех рецептов в категории "салаты", добавленных в избранное
    любым пользователем сайта, отличным от текущего пользователя.
    Функция принимает два параметра:
    :param request - запрос, из которого берётся информация о текущем пользователе;
    :param pk - идентификатор пользователя, чьи избранные рецепты надо отобразить.
    Функция получает из базы данных набор рецептов в категории "салаты", добавленных в избранное пользователем,
    чей идентификатор был передан функции, для каждого рецепта актуализирует состояние лайка/избранного
    (лайкнут ли пост/добавлен ли в избранное текущим пользователем), а также добавляет к набору рецептов пагинацию.
    Функция возвращает веб-страницу с шаблоном user_favs_salads.html и контекстом, содержащим два набора рецептов:
    - набор избранных рецептов с пагинацией (paged_recipes), который отображается на веб-странице;
    - набор со всеми избранными рецептами без пагинации (fav_recipes), который нужен для отображения
    общего количества избранных рецептов;
    а также словарь 'user' с информацией о запрошенном пользователе
    (для отображения никнейма запрошенного пользователя).
    """
    user = get_user_by_id(pk)
    fav_recipes = get_salads(get_all_users_favs(pk))
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_salads.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})


def show_user_favs_first_course(request, pk):
    """
    Функция-представление для отображения списка всех рецептов в категории "первое блюдо", добавленных в избранное
    любым пользователем сайта, отличным от текущего пользователя.
    Функция принимает два параметра:
    :param request - запрос, из которого берётся информация о текущем пользователе;
    :param pk - идентификатор пользователя, чьи избранные рецепты надо отобразить.
    Функция получает из базы данных набор рецептов в категории "первое блюдо", добавленных в избранное пользователем,
    чей идентификатор был передан функции, для каждого рецепта актуализирует состояние лайка/избранного
    (лайкнут ли пост/добавлен ли в избранное текущим пользователем), а также добавляет к набору рецептов пагинацию.
    Функция возвращает веб-страницу с шаблоном user_favs_first_course.html и контекстом, содержащим два набора рецептов:
    - набор избранных рецептов с пагинацией (paged_recipes), который отображается на веб-странице;
    - набор со всеми избранными рецептами без пагинации (fav_recipes), который нужен для отображения
    общего количества избранных рецептов;
    а также словарь 'user' с информацией о запрошенном пользователе
    (для отображения никнейма запрошенного пользователя).
    """
    user = get_user_by_id(pk)
    fav_recipes = get_first_courses(get_all_users_favs(pk))
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_first_course.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})


def show_user_favs_main_course(request, pk):
    """
    Функция-представление для отображения списка всех рецептов в категории "второе блюдо", добавленных в избранное
    любым пользователем сайта, отличным от текущего пользователя.
    Функция принимает два параметра:
    :param request - запрос, из которого берётся информация о текущем пользователе;
    :param pk - идентификатор пользователя, чьи избранные рецепты надо отобразить.
    Функция получает из базы данных набор рецептов в категории "второе блюдо", добавленных в избранное пользователем,
    чей идентификатор был передан функции, для каждого рецепта актуализирует состояние лайка/избранного
    (лайкнут ли пост/добавлен ли в избранное текущим пользователем), а также добавляет к набору рецептов пагинацию.
    Функция возвращает веб-страницу с шаблоном user_favs_main_course.html и контекстом, содержащим два набора рецептов:
    - набор избранных рецептов с пагинацией (paged_recipes), который отображается на веб-странице;
    - набор со всеми избранными рецептами без пагинации (fav_recipes), который нужен для отображения
    общего количества избранных рецептов;
    а также словарь 'user' с информацией о запрошенном пользователе
    (для отображения никнейма запрошенного пользователя).
    """
    user = get_user_by_id(pk)
    fav_recipes = get_main_courses(get_all_users_favs(pk))
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_main_course.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})


def show_user_favs_dessert(request, pk):
    """
    Функция-представление для отображения списка всех рецептов в категории "десерты", добавленных в избранное
    любым пользователем сайта, отличным от текущего пользователя.
    Функция принимает два параметра:
    :param request - запрос, из которого берётся информация о текущем пользователе;
    :param pk - идентификатор пользователя, чьи избранные рецепты надо отобразить.
    Функция получает из базы данных набор рецептов в категории "десерты", добавленных в избранное пользователем,
    чей идентификатор был передан функции, для каждого рецепта актуализирует состояние лайка/избранного
    (лайкнут ли пост/добавлен ли в избранное текущим пользователем), а также добавляет к набору рецептов пагинацию.
    Функция возвращает веб-страницу с шаблоном user_favs_dessert.html и контекстом, содержащим два набора рецептов:
    - набор избранных рецептов с пагинацией (paged_recipes), который отображается на веб-странице;
    - набор со всеми избранными рецептами без пагинации (fav_recipes), который нужен для отображения
    общего количества избранных рецептов;
    а также словарь 'user' с информацией о запрошенном пользователе
    (для отображения никнейма запрошенного пользователя).
    """
    user = get_user_by_id(pk)
    fav_recipes = get_desserts(get_all_users_favs(pk))
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_dessert.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})


def show_user_favs_bakery(request, pk):
    """
    Функция-представление для отображения списка всех рецептов в категории "выпечка", добавленных в избранное
    любым пользователем сайта, отличным от текущего пользователя.
    Функция принимает два параметра:
    :param request - запрос, из которого берётся информация о текущем пользователе;
    :param pk - идентификатор пользователя, чьи избранные рецепты надо отобразить.
    Функция получает из базы данных набор рецептов в категории "выпечка", добавленных в избранное пользователем,
    чей идентификатор был передан функции, для каждого рецепта актуализирует состояние лайка/избранного
    (лайкнут ли пост/добавлен ли в избранное текущим пользователем), а также добавляет к набору рецептов пагинацию.
    Функция возвращает веб-страницу с шаблоном user_favs_bakery.html и контекстом, содержащим два набора рецептов:
    - набор избранных рецептов с пагинацией (paged_recipes), который отображается на веб-странице;
    - набор со всеми избранными рецептами без пагинации (fav_recipes), который нужен для отображения
    общего количества избранных рецептов;
    а также словарь 'user' с информацией о запрошенном пользователе
    (для отображения никнейма запрошенного пользователя).
    """
    user = get_user_by_id(pk)
    fav_recipes = get_bakery(get_all_users_favs(pk))
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_bakery.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})


def show_user_favs_beverages(request, pk):
    """
    Функция-представление для отображения списка всех рецептов в категории "напитки", добавленных в избранное
    любым пользователем сайта, отличным от текущего пользователя.
    Функция принимает два параметра:
    :param request - запрос, из которого берётся информация о текущем пользователе;
    :param pk - идентификатор пользователя, чьи избранные рецепты надо отобразить.
    Функция получает из базы данных набор рецептов в категории "напитки", добавленных в избранное пользователем,
    чей идентификатор был передан функции, для каждого рецепта актуализирует состояние лайка/избранного
    (лайкнут ли пост/добавлен ли в избранное текущим пользователем), а также добавляет к набору рецептов пагинацию.
    Функция возвращает веб-страницу с шаблоном user_favs_beverages.html и контекстом, содержащим два набора рецептов:
    - набор избранных рецептов с пагинацией (paged_recipes), который отображается на веб-странице;
    - набор со всеми избранными рецептами без пагинации (fav_recipes), который нужен для отображения
    общего количества избранных рецептов;
    а также словарь 'user' с информацией о запрошенном пользователе
    (для отображения никнейма запрошенного пользователя).
    """
    user = get_user_by_id(pk)
    fav_recipes = get_beverages(get_all_users_favs(pk))
    check_likes_faves(request, fav_recipes)
    paged_recipes = get_paginated(request, fav_recipes)
    return render(request, 'user-favs/user_favs_beverages.html',
                  {'paged_recipes': paged_recipes,
                   'fav_recipes': fav_recipes,
                   'user': user})
