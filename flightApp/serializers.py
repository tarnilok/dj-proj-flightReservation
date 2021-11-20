from rest_framework import serializers
from .models import Flights, Passengers, Reservation

class FlightsSerializer(serializers.ModelSerializer):
    currentNumberOfPassengers = serializers.SerializerMethodField()
    class Meta:
        model = Flights
        fields = ['flightNumber', 'operatingAirlines', 'departureCity', 'arrivalCity', 'dateOfDeparture', 'estimatedTimeOfDeparture', 'currentNumberOfPassengers']
        
    def get_currentNumberOfPassengers(self, obj):
        return Passengers.objects.filter(flight_id = obj.id).count() 
            
class PassengerSerializer(serializers.ModelSerializer):
    passenger = serializers.StringRelatedField()
    flight = serializers.StringRelatedField()
    class Meta:
        model = Passengers
        fields = '__all__'
        
class ReservationSerializer(serializers.ModelSerializer):
    # passengers = PassengerSerializer(many=True)
    
    user = serializers.StringRelatedField()
    flight_name = serializers.StringRelatedField()
    flight_name_id = serializers.IntegerField()
    class Meta:
        model = Reservation
        fields = '__all__'
        # fields = ['user', 'flight_name', 'first_name', 'last_name', 'email', 'phone', 'created_date', 'updated_date', 'passengers']
        
    # def create(self, validated_data):
    #     passengers_data =validated_data.pop('passengers')
    #     reservation = Reservation.objects.create(**validated_data)
    #     for passenger_data in passengers_data:
    #         Passengers.objects.create(reservation=reservation, **passenger_data)
    #     return reservation