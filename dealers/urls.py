# dealers/urls.py
from django.urls import path
from .views import add_dealer, get_dealers

urlpatterns = [
    path('dealers/', get_dealers, name='get_dealers'),
    path('dealers/add/', add_dealer, name='add_dealer'),
]