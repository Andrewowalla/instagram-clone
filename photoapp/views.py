from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from photoapp.forms import UserRegistrationForm, UserLoginForms

# Create your views here.

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