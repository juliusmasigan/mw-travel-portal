import settings

from django.db import models


# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255, required=True)
    location = models.CharField(max_length=255)

class HotelBooking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT)
    booking_date = models.DateField(auto_now_add=True, editable=False)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=3, choices=settings.SUPPORTED_CURRENCIES)
