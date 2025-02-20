from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('cart/', views.show_cart, name='cart'),  
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'), 
    path('remove_from_cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
