from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm

from .models import *

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required



def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			username= form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username,email=user.email, password=raw_password)
			login(request, user)
			messages.success(request,f'Account created')
			return redirect('app1:login')
	else:
		form = SignUpForm()
	return render(request, 'users/register.html', {'form': form})

	







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
    cart_product_form = CartAddProductForm()
    return render(request,
                  'app1/books/book_detail.html',
                  {'book': book,'cart_product_form': cart_product_form
                   })





