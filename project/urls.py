from django.contrib import admin
from django.urls import path
from main.views import home, new_detail, new_by_categories, add_new
from django.conf.urls.static import static

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('new/add/', add_new, name='add_new'),
    path('category/<int:category_id>/', new_by_categories, name='category_new'),
    path('new/<int:new_id>/', new_detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)