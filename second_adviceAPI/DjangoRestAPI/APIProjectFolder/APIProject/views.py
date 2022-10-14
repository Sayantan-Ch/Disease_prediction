
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

def home_page(request):
    return render(request,"home.html")

def leasing_page(request):
    return render(request,"leasing.html")