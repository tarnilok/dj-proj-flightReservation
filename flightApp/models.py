from django.db import models
from django.contrib.auth.models import User

class Flights(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField(auto_now=False, auto_now_add=False)
    estimatedTimeOfDeparture = models.TimeField(auto_now=False, auto_now_add=False)
    
    def __str__ (self):
        return self.flightNumber
    class Meta:
        verbose_name_plural = "Flights"
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight_name = models.ForeignKey(Flights, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return f"{self.last_name} {self.first_name}"
    
class Passengers(models.Model):
    passenger = models.ForeignKey(Reservation,  on_delete=models.CASCADE)
    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)   
    class Meta:
        verbose_name_plural = "Passengers"
    
    


