# Generated by Django 5.1.3 on 2024-11-18 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0004_alter_populardestination_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='PopularDestination',
        ),
    ]
