
from django.core.paginator import Paginator
from django.db.models import Count, F
from django.shortcuts import render

from recipeblog.models import User
from recipeblog.utils import get_all_users, get_paginated


def sort_user_list_by_reg_date_asc(request):
    users = get_all_users().order_by(F('registration_date').asc())
    paged_users = get_paginated(request, users)
    return render(request, 'user-list/user-list-sort-by-reg-date-asc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_reg_date_desc(request):
    users = get_all_users().order_by(F('registration_date').desc())
    paged_users = get_paginated(request, users)
    return render(request, 'user-list/user-list-sort-by-reg-date-desc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_username_asc(request):
    users = get_all_users().order_by(F('username').asc())
    paged_users = get_paginated(request, users)
    return render(request, 'user-list/user-list-sort-by-username-asc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_username_desc(request):
    users = get_all_users().order_by(F('username').desc())
    users_with_recipes = User.objects.annotate(num_recipes=Count('recipe'))
    paged_users = get_paginated(request, users)
    return render(request, 'user-list/user-list-sort-by-username-desc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_recipes_amount_asc(request):
    users = get_all_users().order_by(F('num_recipes').asc())
    paged_users = get_paginated(request, users)
    return render(request, 'user-list/user-list-sort-by-recipes-amount-asc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_recipes_amount_desc(request):
    users = get_all_users().order_by(F('num_recipes').desc())
    paged_users = get_paginated(request, users)
    return render(request, 'user-list/user-list-sort-by-recipes-amount-desc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_rating_asc(request):
    users = get_all_users().order_by(F('likes_amount').asc())
    paged_users = get_paginated(request, users)
    return render(request, 'user-list/user-list-sort-by-rating-asc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })

def sort_user_list_by_rating_desc(request):
    users = get_all_users().order_by(F('likes_amount').desc())
    paged_users = get_paginated(request, users)
    return render(request, 'user-list/user-list-sort-by-rating-desc.html',
                  {'users': users,
                   'paged_users': paged_users,
                   })