from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


app_name='app1'



urlpatterns=[
    
    path('',views.index_page,name='index_page'),
		path('book_list/',views.book_list,name='book_list'),
	
	   
    path('book_list/<slug:category_slug>/', views.book_list, 
         name='book_list_by_category'),
    path('book_list/<int:id>/<slug:slug>/', views.book_detail,
         name='book_detail'),
		 
		 		path('register/',views.signup,name="register"),
	path('login/',auth_views.LoginView.as_view(template_name="users/login.html"),name="login"),
	path('logout/',auth_views.LogoutView.as_view(template_name="users/logout.html"),name="logout"),
	path('password-reset/',

         auth_views.PasswordResetView.as_view(

             template_name='users/password_reset.html'

         ),

         name='password_reset'),
		 
		  path('password-reset/done/',

         auth_views.PasswordResetDoneView.as_view(

             template_name='users/password_reset_done.html'

         ),

         name='password_reset_done'),
		 
		  path('password-reset-confirm/<uidb64>/<token>/',

         auth_views.PasswordResetConfirmView.as_view(

             template_name='users/password_reset_confirm.html'

         ),

         name='password_reset_confirm'),
		 path('password-reset-complete/',

         auth_views.PasswordResetCompleteView.as_view(

             template_name='users/password_reset_complete.html'

         ),

         name='password_reset_complete'),
    
    
      path('search/',views.search,name='search'),
		 
	
	
	
]