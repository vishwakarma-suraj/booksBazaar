from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls', namespace='app1')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('Sell/', include('Sell.urls', namespace='Sell')),

	
	
	
	
	
	
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

