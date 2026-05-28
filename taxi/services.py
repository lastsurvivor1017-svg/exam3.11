from rest_framework import serializers
from .models import Ride

class RideSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ride
        fields = '__all__'
        read_only_fields = ['user', 'driver', 'price', 'status']


def calculate_price(distance):
    base_price = 30
    per_km = 10
    return base_price + (distance * per_km)

