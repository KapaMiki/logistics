from django.urls import path
from .views import index, calculation, order, about, services, packing, order_status


urlpatterns = [
    path('', index, name='index_url'),
    path('calculation/', calculation, name='calculation_url'),
    path('order/', order, name='order_url'),
    path('about/', about, name='about_url'),
    path('services/', services, name='services_url'),
    path('packing/', packing, name='packing_url'),
    path('order-status/', order_status, name='order_status_url')
]
