from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import Passengers, Reservation, Flights
from .serializers import PassengerSerializer, ReservationSerializer, FlightsSerializer

def home(request):
    return HttpResponse('<center><h1 style="background-color:powderblue;">Welcome to the Flight API</h1></center>')

class PassengerViewSet(ModelViewSet):
    queryset = Passengers.objects.all()
    serializer_class = PassengerSerializer
    
class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
class FlightViewSet(ModelViewSet):
    queryset = Flights.objects.all()
    serializer_class = FlightsSerializer


