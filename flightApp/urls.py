from django.urls import path, include
from .views import home, FlightViewSet, ReservationViewSet, PassengerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('flights', FlightViewSet)
router.register('reservations', ReservationViewSet)
router.register('passengers', PassengerViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls)),
]
