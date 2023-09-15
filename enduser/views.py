
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'pages/index.html')

def apartment(request):
    return render(request, 'pages/property-apartment.html')

def room(request):
    return render(request, 'pages/property-room.html')

def commerce(request):
    return render(request, 'pages/property-commerce.html')

def land(request):
    return render(request, 'pages/property-land.html')

def house(request):
    return render(request, 'pages/property-house.html')


def vehicle(request):
    return render(request, 'pages/property-vehicle.html')

def single(request):
    return render(request, 'pages/property-single2.html')

def contact(request):
    return render(request, 'pages/contact.html')

def history(request):
    return render(request, 'pages/comingsoon.html')

def team(request):
    return render(request, 'pages/comingsoon.html')

def get_job(request):
    return render(request, 'pages/comingsoon.html')

def blog(request):
    return render(request, 'pages/comingsoon.html')
