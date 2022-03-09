from multiprocessing import context
from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from photoapp.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home_view(request):
    return render(request, 'registration/dashboard.html')

def homepage(request):
    images = Image.objects.all()
    return render(request, 'home.html', {"images":images})

def register(request):
    context = {}
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context['register_form'] = form

    else:
        form = UserRegistrationForm()
        context['register_form'] = form

    return render(request, "registration/register.html", context)

def login_view(request):
    context = {}
    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
            return redirect("dashboard")
    else:
        form = UserLoginForm()
        context['login_form'] = form
    return render(request, "registration/login.html", context)

def logout_view(request):
    logout(request)
    return redirect('login')