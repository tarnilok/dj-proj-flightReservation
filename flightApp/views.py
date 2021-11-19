from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework import pagination
from rest_framework.viewsets import ModelViewSet
from .models import Passengers, Reservation, Flights
from .serializers import PassengerSerializer, ReservationSerializer, FlightsSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import FlightPagination, ReservationPagination, PassengersPagination

def home(request):
    return HttpResponse('<center><h1 style="background-color:powderblue;">Welcome to the Flight API</h1></center>')

class PassengerViewSet(ModelViewSet):
    queryset = Passengers.objects.all().order_by('flight')
    serializer_class = PassengerSerializer
    pagination_class = PassengersPagination
    
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['passenger__first_name', 'passenger__last_name']
    ordering_fields = ['passenger']
    
class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all().order_by('user')
    serializer_class = ReservationSerializer
    pagination_class = ReservationPagination
    
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name']
    
class FlightViewSet(ModelViewSet):
    queryset = Flights.objects.all().order_by('flightNumber')
    serializer_class = FlightsSerializer
    pagination_class = FlightPagination
    
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['flightNumber', 'operatingAirlines', 'departureCity', 'arrivalCity']
    ordering_fields = ['dateOfDeparture']


