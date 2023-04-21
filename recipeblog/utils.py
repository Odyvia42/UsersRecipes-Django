from django.core.paginator import Paginator


def get_all_my_favs(request):
    return request.user.recipe_favs.all()

def get_paginated(request, queryset):
    p = Paginator(queryset, 5)
    page = request.GET.get('page')
    return p.get_page(page)
