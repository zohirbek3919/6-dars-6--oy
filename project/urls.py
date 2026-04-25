from django.contrib import admin
from django.urls import path, include
from main.views import home, car_detail, brand_car
from django.conf.urls.static import static

from . import settings

urlpatterns = [
    path('', home, name='home'),
    path('brand/<int:brand_id>/', brand_car, name='brand_car'),
    path('car/<int:car_id>/', car_detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
