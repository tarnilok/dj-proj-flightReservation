from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse('<center><h1 style="background-color:powderblue;">accounts</h1></center>')

