from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from rest_framework import pagination
from rest_framework.viewsets import ModelViewSet
from .models import Passengers, Reservation, Flights
from .serializers import PassengerSerializer, ReservationSerializer, FlightsSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import FlightPagination, ReservationPagination, PassengersPagination
from .permissions import IsAdminOrReadOnly, IsAddedByUserOrReadOnly, IsSuperOrNotAllowed

def home(request):
    return redirect('/swagger/')

class PassengerViewSet(ModelViewSet):
    queryset = Passengers.objects.all().order_by('flight')
    serializer_class = PassengerSerializer
    # pagination_class = PassengersPagination
    permission_classes = [IsSuperOrNotAllowed]

    
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['passenger__first_name', 'passenger__last_name']
    ordering_fields = ['passenger']
    
class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all().order_by('user')
    serializer_class = ReservationSerializer
    # pagination_class = ReservationPagination
    permission_classes = [IsAddedByUserOrReadOnly]
    
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name']
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class FlightViewSet(ModelViewSet):
    queryset = Flights.objects.all().order_by('flightNumber')
    serializer_class = FlightsSerializer
    # pagination_class = FlightPagination
    permission_classes = [IsAdminOrReadOnly]
    
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['flightNumber', 'operatingAirlines', 'departureCity', 'arrivalCity']
    ordering_fields = ['dateOfDeparture']


