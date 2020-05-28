from django.shortcuts import render
from django.http import HttpResponse
from .models import Order
from apps.trucks.models import Truck
from apps.locations.models import City



def index(request):
    Order.objects.create(
        first_name='qwe',
        last_name='qwe',
        middle_name='qwe',
        email='qwdqwd@mail.ru',
        phone='qweqwd',
        truck=Truck.objects.first(),
        departure=City.objects.first(),
        arrival=City.objects.last()
    )
    return HttpResponse('<h1>WQEQWE</h1>')