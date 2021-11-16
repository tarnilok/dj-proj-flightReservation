from rest_framework import serializers
from .models import Flights, Passengers, Reservation

class FlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = '__all__'
        
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passengers
        fields = '__all__'
        
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'