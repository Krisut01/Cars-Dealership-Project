from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_dealers, name='get_dealers'),
    path('<int:dealer_id>/', views.get_dealer_by_id, name='get_dealer_by_id'),
    path('state/<str:state>/', views.get_dealers_by_state, name='get_dealers_by_state'),
    path('makes/', views.get_car_makes, name='get_car_makes'),
]
