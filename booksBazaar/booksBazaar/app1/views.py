from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

from .models import *


def index_page(request):
    return render(request, 'app1/books/index.html')


def login(request):
    c = {}
    return render(request, 'login.html', c)


def loggedin(request):
    return render(request, 'loggedin.html', {'full_name': request.user.username})


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')


def invalid_login(request):
    return render(request, 'invalid_login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')
