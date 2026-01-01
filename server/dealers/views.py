from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
import json
from .models import Dealer, CarMake, CarModel
from reviews.models import Review

@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealers(request):
    """Get all dealers"""
    dealers = Dealer.objects.all()
    dealer_data = []

    for dealer in dealers:
        dealer_data.append({
            'id': dealer.id,
            'name': dealer.name,
            'address': dealer.address,
            'city': dealer.city,
            'state': dealer.state,
            'zip_code': dealer.zip_code,
            'phone': dealer.phone,
            'website': dealer.website,
        })

    return Response(dealer_data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealer_by_id(request, dealer_id):
    """Get dealer by ID"""
    try:
        dealer = Dealer.objects.get(id=dealer_id)
        dealer_data = {
            'id': dealer.id,
            'name': dealer.name,
            'address': dealer.address,
            'city': dealer.city,
            'state': dealer.state,
            'zip_code': dealer.zip_code,
            'phone': dealer.phone,
            'website': dealer.website,
        }
        return Response(dealer_data)
    except Dealer.DoesNotExist:
        return Response({'error': 'Dealer not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealers_by_state(request, state):
    """Get dealers by state"""
    dealers = Dealer.objects.filter(state__iexact=state)
    dealer_data = []

    for dealer in dealers:
        dealer_data.append({
            'id': dealer.id,
            'name': dealer.name,
            'address': dealer.address,
            'city': dealer.city,
            'state': dealer.state,
            'zip_code': dealer.zip_code,
            'phone': dealer.phone,
            'website': dealer.website,
        })

    return Response(dealer_data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_car_makes(request):
    """Get all car makes and models"""
    makes = CarMake.objects.all()
    make_data = []

    for make in makes:
        models = CarModel.objects.filter(make=make)
        model_data = [{'id': model.id, 'name': model.name} for model in models]
        make_data.append({
            'id': make.id,
            'name': make.name,
            'models': model_data
        })

    return Response(make_data)
