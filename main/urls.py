from django.urls import path
from .views import home, new_detail, new_by_categories, add_new

urlpatterns = [
    path('', home, name='home'),
    path('new/add/', add_new, name='add_new'),
    path('new/<int:new_id>/', new_detail, name='new_detail'),
    path('category/<int:category_id>/', new_by_categories, name='category_new'),
]