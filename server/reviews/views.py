from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import json
from .models import Review
from dealers.models import Dealer

@api_view(['GET'])
@permission_classes([AllowAny])
def get_dealer_reviews(request, dealer_id):
    """Get all reviews for a specific dealer"""
    try:
        dealer = Dealer.objects.get(id=dealer_id)
        reviews = Review.objects.filter(dealer=dealer)
        review_data = []

        for review in reviews:
            review_data.append({
                'id': review.id,
                'user': review.user.username,
                'review_text': review.review_text,
                'purchase': review.purchase,
                'purchase_date': review.purchase_date,
                'car_make': review.car_make,
                'car_model': review.car_model,
                'car_year': review.car_year,
                'sentiment': review.sentiment,
                'created_at': review.created_at,
            })

        return Response(review_data)
    except Dealer.DoesNotExist:
        return Response({'error': 'Dealer not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_review(request):
    """Post a new review for a dealer"""
    try:
        data = request.data
        dealer_id = data.get('dealer_id')
        review_text = data.get('review_text')

        if not dealer_id or not review_text:
            return Response({'error': 'Dealer ID and review text are required'}, status=status.HTTP_400_BAD_REQUEST)

        dealer = Dealer.objects.get(id=dealer_id)

        review = Review.objects.create(
            dealer=dealer,
            user=request.user,
            review_text=review_text,
            purchase=data.get('purchase', False),
            purchase_date=data.get('purchase_date'),
            car_make=data.get('car_make'),
            car_model=data.get('car_model'),
            car_year=data.get('car_year'),
        )

        return Response({
            'id': review.id,
            'message': 'Review posted successfully'
        }, status=status.HTTP_201_CREATED)

    except Dealer.DoesNotExist:
        return Response({'error': 'Dealer not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def analyze_review(request):
    """Analyze sentiment of review text"""
    text = request.data.get('text', '')
    if not text:
        return Response({'error': 'Text is required'}, status=status.HTTP_400_BAD_REQUEST)

    # Simple sentiment analysis (you can replace with a more sophisticated model)
    sentiment = analyze_sentiment(text)

    return Response({
        'text': text,
        'sentiment': sentiment
    })

def analyze_sentiment(text):
    """Simple sentiment analysis - replace with actual ML model"""
    positive_words = ['fantastic', 'great', 'excellent', 'good', 'amazing', 'wonderful', 'love', 'best']
    negative_words = ['terrible', 'bad', 'awful', 'horrible', 'worst', 'hate', 'disappointed']

    text_lower = text.lower()
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)

    if positive_count > negative_count:
        return 'positive'
    elif negative_count > positive_count:
        return 'negative'
    else:
        return 'neutral'
