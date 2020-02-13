from django.urls import path
from .import views


app_name='app1'



urlpatterns=[
    
    path('',views.index_page,name='index_page'),
	path('book_list/',views.book_list,name='book_list'),
	   
    path('book_list/<slug:category_slug>/', views.book_list, 
         name='book_list_by_category'),
    path('book_list/<int:id>/<slug:slug>/', views.book_detail,
         name='book_detail'),
	
   
]