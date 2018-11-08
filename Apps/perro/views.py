from django.shortcuts import render
from django.utils import timezone
from .models import Perro
from django.contrib.auth import authenticate, login
from .forms import PostContacto


# Create your views here.
def index(request):
    return render(request, 'MisPerris/index.html')

def contacto(request):
    form = PostContacto
    return render(request, 'MisPerris/contacto.html')

def index_login(request):
    return render(request,'registration/login.html')

def index_logged_out(request):
    return render(request, 'registration/logged_out.html')