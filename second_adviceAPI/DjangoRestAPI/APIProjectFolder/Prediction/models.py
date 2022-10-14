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