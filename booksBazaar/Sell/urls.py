from django.urls import path
from . import views


app_name = 'Sell'
urlpatterns = [

      path('', views.post_list, name='post_list'),
      path('<int:id>/',views.post_detail,name='post_detail'),
    path('create/', views.post_create, name='post_create'),
     path('<int:id>/edit',views.post_update,name='post_update'),
        path('<int:id>/delete/', views.post_delete, name='post_delete'),


]