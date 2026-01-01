#!/usr/bin/env python
import os
import django
import sys

# Setup Django
sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
django.setup()

from dealers.models import Dealer, CarMake, CarModel
from django.contrib.auth.models import User

def populate_data():
    # Create superuser
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')

    # Create sample dealers
    dealers_data = [
        {
            'name': 'Premium Auto Dealership',
            'address': '123 Main Street',
            'city': 'Anytown',
            'state': 'California',
            'zip_code': '12345',
            'phone': '(555) 123-4567',
            'website': 'https://premiumauto.com'
        },
        {
            'name': 'City Motors',
            'address': '456 Oak Avenue',
            'city': 'Springfield',
            'state': 'Kansas',
            'zip_code': '67890',
            'phone': '(555) 987-6543',
            'website': 'https://citymotors.com'
        },
        {
            'name': 'Elite Cars',
            'address': '789 Pine Road',
            'city': 'Riverside',
            'state': 'California',
            'zip_code': '54321',
            'phone': '(555) 456-7890',
            'website': 'https://elitecars.com'
        }
    ]

    for dealer_data in dealers_data:
        Dealer.objects.get_or_create(
            name=dealer_data['name'],
            defaults=dealer_data
        )

    # Create car makes and models
    car_data = {
        'Toyota': ['Camry', 'Corolla', 'RAV4', 'Highlander'],
        'Honda': ['Civic', 'Accord', 'CR-V', 'Pilot'],
        'Ford': ['F-150', 'Mustang', 'Explorer', 'Focus'],
        'Chevrolet': ['Silverado', 'Malibu', 'Equinox', 'Tahoe'],
        'BMW': ['3 Series', '5 Series', 'X3', 'X5'],
        'Mercedes-Benz': ['C-Class', 'E-Class', 'GLC', 'GLE']
    }

    for make_name, models in car_data.items():
        make, created = CarMake.objects.get_or_create(name=make_name)
        for model_name in models:
            CarModel.objects.get_or_create(make=make, name=model_name)

    print("Sample data populated successfully!")

if __name__ == '__main__':
    populate_data()
