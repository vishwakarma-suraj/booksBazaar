from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

from .models import *


def index_page(request):
    return render(request, 'app1/books/index.html')
	

	
	
def book_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    books = Book.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = books.filter(category=category)
    return render(request,
                  'app1/books/book_list.html',
                  {'category': category,
                   'categories': categories,
                   'books': books})


def book_detail(request, id, slug):
    book = get_object_or_404(Book,
                                id=id,
                                slug=slug
                                )
    
    return render(request,
                  'app1/books/book_detail.html',
                  {'book': book,
                   })




def login(request):
    c = {}
    return render(request, 'app1/books/login.html', c)


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
