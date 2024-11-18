from django.shortcuts import render, redirect

# Create your views here.
from .models import *
# from .forms import *


def home(request):
    return render(request, template_name='home.html')


def about_us(request):
    return render(request, template_name='about_us.html')


def book(request):
    return render(request, template_name='book.html')


def log_in(request):
    return render(request, template_name='log_in.html')


def sign_up(request):
    return render(request, template_name='sign_up.html')


def popular_destination(request):
    popular_destinations = PopularDestination.objects.all()
    context = {'popular_destinations': popular_destinations}
    return render(request, template_name='popular_destination.html', context=context)
