from django.urls import path
from . import views

urlpatterns = [
    path('dealer/<int:dealer_id>/', views.get_dealer_reviews, name='get_dealer_reviews'),
    path('post/', views.post_review, name='post_review'),
    path('analyze/', views.analyze_review, name='analyze_review'),
]
