from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.forms import ModelForm
from .models import Recipe


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class RecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = ('title', 'dish_type', 'description', 'ingredients', 'steps_to_complete', 'picture', 'tags')
        labels = {
            'title': 'Название',
            'dish_type': 'Тип блюда',
            'description': 'Описание',
            'ingredients': 'Ингредиенты',
            'steps_to_complete': 'Пошаговая инструкция',
            'picture': 'Фото',
            'tags': 'Теги'
        }


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {
            'username': 'Имя пользователя',
            'email': 'Электронная почта',
            'password': 'Пароль'
        }
