from django.shortcuts import render,get_object_or_404
from .models import *


def index_page(request):
    return render(request,'app1/books/index.html')





