from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')