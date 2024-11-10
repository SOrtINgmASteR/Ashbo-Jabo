from django.shortcuts import render

# Create your views here.
from .models import *


def home(request):
    return render(request, template_name='home.html')


def book(request):
    return render(request, template_name='book.html')


def popular_destinations(request):
    popular_destination = PopularDestination.objects.all()
    context = {
        'popular_destination': popular_destination,
    }
    return render(request, template_name='popular_destinations.html', context=context)


def about_us(request):
    return render(request, template_name='about_us.html')