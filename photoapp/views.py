from multiprocessing import context
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect
from photoapp.forms import UserRegistrationForm, UserLoginForm, NewImageForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# def home_view(request):
#     return render(request, 'registration/dashboard.html')

def homepage(request):
    images = Image.objects.all()
    return render(request, 'home.html', {"images":images})

def search_results(request):
    if 'profile' in request.GET and request.GET['profile']:
        search_query = request.GET.get('profile')
        searched_profiles = Profile.search_profile(search_query)
        message = f'{search_query}'
        context = {
           'message':message,
           'searched_profiles':searched_profiles
        }

        return render (request, 'search.html', context)
    else:
        message = 'You havent searched for any profile'
        return render(request, 'search.html', {'message':message})

def new_image(request):
    current_user = request.user
    image = Image(user = request.user )
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES, instance= image)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('homepage')
    else:
        form = NewImageForm()
        context = {
            'form':form
        }
        return render(request, 'new_image.html', context)

def image(request, id):
    try:
        image = Image.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404()
    comments = image.comment_set.all()

    if request.method == 'POST':
        comment = Comment.objects.create (
            user = request.user,
            image = image,
            comment = request.POST.get('comment')
        )

        return redirect('homepage')
    context = {
        'image':image,
        'comments': comments
    }
    return render(request, 'image.html', context)

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

            try:
                user = Profile.objects.get(email = email)
            except:
                messages.error(request, 'user does not exist')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
            return redirect("homepage")
    else:
        messages.error(request, 'Username or Password does not exist')
        form = UserLoginForm()
        context['login_form'] = form
    return render(request, "registration/login.html", context)

def logout_view(request):
    logout(request)
    return redirect('login')