# Generated by Django 5.1.3 on 2024-11-10 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_location', models.CharField(max_length=100)),
                ('departure_time', models.TimeField()),
                ('destination_location', models.CharField(max_length=100)),
                ('destination_time', models.TimeField()),
                ('travel_date', models.DateField()),
                ('service_name', models.CharField(max_length=255)),
                ('booking_date', models.DateField()),
                ('price', models.FloatField()),
                ('travel_time_hour', models.IntegerField()),
                ('travel_time_minutes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PopularDestination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_image', models.ImageField(upload_to='destinations/')),
                ('departure_location', models.CharField(max_length=100)),
                ('departure_time', models.TimeField()),
                ('destination_location', models.CharField(max_length=100)),
                ('destination_time', models.TimeField()),
                ('travel_date', models.DateField()),
                ('service_name', models.CharField(max_length=255)),
                ('booking_date', models.DateField()),
                ('price', models.FloatField()),
                ('travel_time_hour', models.IntegerField()),
                ('travel_time_minutes', models.IntegerField()),
            ],
        ),
    ]
