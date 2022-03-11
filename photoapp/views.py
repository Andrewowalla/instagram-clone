from multiprocessing import context
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.urls import reverse
from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect
from photoapp.forms import UserRegistrationForm, NewImageForm, LoginForm, UpdateProfileForm
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

def view_profile(request, id):
    try:
        profile = Profile.objects.get(id = id)
        context = {
            'profile': profile,                       
        }
        return render(request, 'profile.html', context)
    except:
        messages.warning(request, 'Sorry, but it seems the profile is not set up')
        return redirect('homepage')


def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect(reverse('view_profile', kwargs={"id": request.user.profile.id }))
        else:
            messages.warning(request, 'There was a problem updating your profile')
            return redirect('update_profile')
    else:
        form = UpdateProfileForm(instance=request.user.profile)
        return render(request, 'update_profile.html', {"form":form})

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
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']


            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
            return redirect("homepage")
        else:
            messages.error(request, 'Username or Password does not exist')
            message = 'Not found'
            form = LoginForm()
            context['login_form'] = form
            context['message'] = message
            return render(request, "registration/login.html", context)
    return render(request, "registration/login.html", context)

def logout_view(request):
    logout(request)
    return redirect('login')