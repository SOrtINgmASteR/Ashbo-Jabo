from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *
from .forms import *

# Create your views here.



def home(request):
    return render(request, template_name='home.html')


def about_us(request):
    return render(request, template_name='about_us.html')


def book(request):
    return render(request, template_name='book.html')


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'log_in.html', {'form': form})


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Assign role (e.g., 'admin', 'staff', or 'user') after registration
            role = request.POST.get('role')
            if role:
                group = Group.objects.get(name=role)
                user.groups.add(group)

            # Log the user in immediately after registration
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})


def custom_logout(request):
    logout(request)
    # Perform any additional actions here (e.g., logging out analytics)
    return redirect('log_in')


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