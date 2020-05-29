from django.shortcuts import render
from apps.locations.models import City
from .models import DefaultPrice
from apps.locations.models import Distance
from django.contrib import messages
from apps.orders.models import Order, Equipment



def index(request):
    return render(request, 'properties/index.html')


def calculation(request):
    cities = City.objects.all()

    if request.method == 'POST':
        default_price = DefaultPrice.objects.first()
        city_a = City.objects.get(id=int(request.POST.get('city_a')))
        city_b = City.objects.get(id=int(request.POST.get('city_b')))


        distance = Distance.objects.filter(cities__in=[city_a, city_b]).first().km

        weight = float(request.POST.get('weight'))
        width = float(request.POST.get('width'))
        height = float(request.POST.get('height'))
        length = float(request.POST.get('length'))

        volume = width * height * length

        weight_price = weight * default_price.kg
        km_price = distance * (default_price.hundred_km / 100)
    
        total = (volume * default_price.cubic_meter) + weight_price + km_price
        messages.success(request, str(total))
        return render(request, 'properties/calculation.html', context={
            'cities':cities
        })
    else:
        return render(request, 'properties/calculation.html', context={
            'cities':cities
        })


def order(request):
    cities = City.objects.all()
    if request.method == 'POST':
        print(request.POST)
        default_price = DefaultPrice.objects.first()
        city_a = City.objects.get(id=int(request.POST.get('city_a')))
        city_b = City.objects.get(id=int(request.POST.get('city_b')))

        email = request.POST.get('email')
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        distance = Distance.objects.filter(cities__in=[city_a, city_b]).first().km

        weight = float(request.POST.get('weight'))
        width = float(request.POST.get('width'))
        height = float(request.POST.get('height'))
        length = float(request.POST.get('length'))
        print(phone, email,name,weight,height,length)

        order = Order.objects.create(
            email=email,
            phone=phone,
            departure=city_a,
            arrival=city_b
        )
        Equipment.objects.create(
            order=order,
            name=name,
            weight=weight,
            width=width,
            height=height,
            length=length
        )
        return render(request, 'properties/order.html', context={
            'cities':cities
        })
    else:
        return render(request, 'properties/order.html', context={
            'cities':cities
        })


def about(request):
    return render(request, 'properties/about.html')


def services(request):
    return render(request, 'properties/services.html')

def packing(request):
    return render(request, 'properties/packing.html')

def order_status(request):
    if request.method == 'POST':
        print(request.POST)
        return render(request, 'properties/order-status.html')
    else:
        return render(request, 'properties/order-status.html')