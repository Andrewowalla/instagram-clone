from django import forms
from django.contrib.auth.forms import UserCreationForm
from photoapp.models import MyUser
from django.contrib.auth import authenticate

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('email', 'username', 'password1', 'password2')