from django.urls import path
from .views import add_dealer, get_dealers, update_dealer, delete_all_dealers

urlpatterns = [
    path('add/', add_dealer, name='add_dealer'),
    path('list/', get_dealers, name='get_dealers'),
    path('update/<int:dealer_id>/', update_dealer, name='update_dealer'),
    path('delete/', delete_all_dealers, name='delete_all_dealers'),
]