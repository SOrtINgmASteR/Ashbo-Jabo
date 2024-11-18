from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import *


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


def add_popular_destination(request):
    form = PopularDestinationForm()
    if request.method == 'POST':
        form = PopularDestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, template_name='popular_destination_form.html', context=context)


def delete_popular_destination(request, id):
    popular_destination = PopularDestination.objects.get(pk=id)
    if request.method == 'POST':
        popular_destination.delete()
        return redirect('popular_destination')
    return render(request, template_name='delete_popular_destination.html')


def update_popular_destination(request,id):
    popular_destination = PopularDestination.objects.get(pk=id)
    form = PopularDestinationForm(instance=popular_destination)
    if request.method == 'POST':
        form = PopularDestinationForm(request.POST, request.FILES, instance=popular_destination)
        if form.is_valid():
            form.save()
            return redirect('popular_destination')
    context = {'form': form}
    return render(request, template_name='popular_destination_form.html', context=context)