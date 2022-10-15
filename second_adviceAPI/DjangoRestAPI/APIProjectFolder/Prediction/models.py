from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length = 100)
    speciality = models.CharField(max_length = 100)
    practice_name = models.CharField(max_length = 100)
    address = models.CharField(max_length=100)
    pincode = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class LeasingInfo(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    info = models.CharField(max_length=400)