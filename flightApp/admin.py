from django.contrib import admin
from .models import Reservation, Passengers, Flights

admin.site.register(Reservation)
admin.site.register(Passengers)
admin.site.register(Flights)
