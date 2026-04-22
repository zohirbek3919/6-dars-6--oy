from django.contrib import admin
from django.urls import path
from main.views import home, car_detail, brand_car

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('brand/<int:brand_id>/', brand_car, name='brand_car'),
    path('car/<int:car_id>/', car_detail, name='car_detail'),
]