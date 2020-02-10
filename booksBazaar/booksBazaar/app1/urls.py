from django.urls import path
from .import views

app_name='app1'



urlpatterns=[
    
    path('',views.index_page,name='index_page'),
   
]