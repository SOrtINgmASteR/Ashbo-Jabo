from django.db import models

# Create your models here.
import uuid


class PopularDestination(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    destination_image = models.ImageField(upload_to='destinations/')
    destination_location = models.CharField(max_length=50)
    departure_location = models.CharField(max_length=50)
    travel_time_maximum = models.IntegerField()
    travel_time_minimum = models.IntegerField()

    def __str__(self):
        return self.departure_location + ' - ' + self.destination_location
