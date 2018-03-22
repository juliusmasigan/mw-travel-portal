import settings
from django.db import models


# Create your models here.

class Transport(models.Model):
    transport_type = models.charField(max_length=255)
