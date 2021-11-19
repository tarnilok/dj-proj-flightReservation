from rest_framework.pagination import PageNumberPagination

class FlightPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'pagenumber'
    page_size_query_param = 'page'
    
class ReservationPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'pagenumber'
    page_size_query_param = 'page_size'
    
class PassengersPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'pagenumber'
    page_size_query_param = 'page_size'