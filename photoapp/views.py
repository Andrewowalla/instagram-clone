from django.shortcuts import render
from .models import *

# Create your views here.

def homepage(request):
    images = Image.objects.all()
    return render(request, 'home.html', {"images":images})

