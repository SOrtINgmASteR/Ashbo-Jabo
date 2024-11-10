from django.db import models

# Create your models here.


class Booking(models.Model):
    departure_location = models.CharField(max_length=100)
    departure_time = models.TimeField()
    destination_location = models.CharField(max_length=100)
    destination_time = models.TimeField()
    travel_date = models.DateField()
    service_name = models.CharField(max_length=255)
    booking_date = models.DateField()
    price = models.FloatField()
    travel_time_hour = models.IntegerField()
    travel_time_minutes = models.IntegerField()

    def __str__(self):
        return self.departure_location + ' - ' + self.destination_location


class PopularDestination(models.Model):
    destination_image = models.ImageField(upload_to='destinations/')
    departure_location = models.CharField(max_length=100)
    departure_time = models.TimeField()
    destination_location = models.CharField(max_length=100)
    destination_time = models.TimeField()
    travel_date = models.DateField()
    service_name = models.CharField(max_length=255)
    booking_date = models.DateField()
    price = models.FloatField()
    travel_time_hour = models.IntegerField()
    travel_time_minutes = models.IntegerField()

    def __str__(self):
        return self.departure_location + ' - ' + self.destination_location
