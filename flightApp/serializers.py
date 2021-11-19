from rest_framework import serializers
from .models import Flights, Passengers, Reservation

class FlightsSerializer(serializers.ModelSerializer):
    currentNumberOfPassengers = serializers.SerializerMethodField()
    class Meta:
        model = Flights
        fields = ['flightNumber', 'operatingAirlines', 'departureCity', 'arrivalCity', 'dateOfDeparture', 'estimatedTimeOfDeparture', 'currentNumberOfPassengers']
        
    def get_currentNumberOfPassengers(self, obj):
        return Passengers.objects.filter(flight_id = obj.id).count() 
       
        
class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    flight_name = serializers.StringRelatedField()
    class Meta:
        model = Reservation
        fields = '__all__'
        
class PassengerSerializer(serializers.ModelSerializer):
    passenger = serializers.StringRelatedField()
    flight = serializers.StringRelatedField()
    class Meta:
        model = Passengers
        fields = '__all__'