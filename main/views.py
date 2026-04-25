from django.shortcuts import render
from .models import Brand, Car

def home(request):
    context = {
        'brands': Brand.objects.all(),
        'cars': Car.objects.all(),
    }
    return render(request, 'main/index.html', context)

def brand_car(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    cars = Car.objects.filter(brand_id=brand_id)

    return render(request, 'main/brand_cars.html', {
        'brand': brand,
        'cars': cars
    })

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'main/detail.html', {'car': car})