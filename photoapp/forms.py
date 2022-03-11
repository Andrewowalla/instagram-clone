from django import forms
from django.contrib.auth.forms import UserCreationForm
from photoapp.models import MyUser
from django.contrib.auth import authenticate
from .models import Image, Profile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('email', 'username', 'password1', 'password2')

# class UserLoginForm(forms.ModelForm):
#     password = forms.CharField(label = "password", widget=forms.PasswordInput)

#     class Meta:
#         model = MyUser
#         fields = ('email', 'password')

#     def clean(self):
#         if self.is_valid():
#             email = self.cleaned_data['email']
#             password = self.cleaned_data['password']

#             if not authenticate(email=email, password=password):
#                 raise forms.ValidationError("invalid credentials")

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['upload_time', 'likes', 'user']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'bio', 'profilepic')
        # exclude = ['user']