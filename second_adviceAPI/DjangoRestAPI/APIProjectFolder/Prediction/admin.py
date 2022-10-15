from django.contrib import admin

# Register your models here.
from .models import Doctor, LeasingInfo

admin.site.register(Doctor)
admin.site.register(LeasingInfo)