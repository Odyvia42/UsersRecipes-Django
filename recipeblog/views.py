from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView

from recipeblog.models import User


# Create your views here.

def index(request: HttpRequest):
    return render(request, 'index.html')


class UserListView(ListView):
    model = User
    context_object_name = 'user_list'
    template_name = 'user-list.html'




