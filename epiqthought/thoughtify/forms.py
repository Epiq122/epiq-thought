from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserLoginForm(AuthenticationForm):
    class Meta:
        username = forms.CharField(widget=TextInput())
        password = forms.CharField(widget=PasswordInput())