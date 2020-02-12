from django.urls import path
from .import views

app_name='app1'



urlpatterns=[
    
    path('',views.index_page,name='index_page'),
	path('book_list/',views.book_list,name='book_list'),
	path('login/',views.login,name='login'),
   
]