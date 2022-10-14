from pyexpat import model
from django.shortcuts import render
from .apps import PredictionConfig
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
import pickle
import numpy as np

# Create your views here.
with open('saved_dictionary.pkl', 'rb') as f:
        data_dict1 = pickle.load(f)


class Disease_Predict(APIView):
    #permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = request.POST["symptom"]
        # print(request.POST)
        # print(data)
        # data["symptoms"]
        symptoms = data
        symptoms = symptoms.split(",")
        diagnostic = symptoms[-1]
        symptoms = symptoms[:-1]
        input_data = [0] * len(data_dict1["symptom_index"])
        for symptom in symptoms:
            index = data_dict1["symptom_index"][symptom]
            input_data[index] = 1

        # reshaping the input data and converting it
        # into suitable format for model predictions
        input_data = np.array(input_data).reshape(1,-1)
        model = PredictionConfig.classifier
        # generating individual outputs
        prediction = data_dict1["predictions_classes"][model.predict(input_data)[0]]
        isTrue = 0
        if prediction == diagnostic:
            isTrue = 0
        else:
            isTrue = 1
        predictions = {
            "model": prediction,
            "doctor": diagnostic,
            "Get second advice": isTrue,
        }
        
        return Response(predictions, status=200)


def secondAdvice_page(request):
    return render(request,"secondAdvice.html")

def check_advice(request):
    if request.method == "POST":
        dict1 = request.POST
        symptoms = request.POST.getlist("array[]")
        # print(dict1)
        # symptoms = list(dict1.values())
        # print(symptoms)
        # print(type(symptoms))
        # symptoms = symptoms.split(",")
        # diagnostic = dict1["doctorA"]
        # symptoms = symptoms[:-1]
        diagnostic = dict1["doctorAdvice"]
        input_data = [0] * len(data_dict1["symptom_index"])
        for symptom in symptoms:
            index = data_dict1["symptom_index"][symptom]
            input_data[index] = 1

        # reshaping the input data and converting it
        # into suitable format for model predictions
        input_data = np.array(input_data).reshape(1,-1)
        model = PredictionConfig.classifier
        # generating individual outputs
        prediction = data_dict1["predictions_classes"][model.predict(input_data)[0]]
        isTrue = 0
        if prediction == diagnostic:
            isTrue = 0
        else:
            isTrue = 1
        predictions = {
            "model": prediction,
            "doctor": diagnostic,
            "Get second advice": isTrue,
        }
        # txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
        context = {"result": "Model : {pred}, Doctor : {diag}, Second advice : {advice}".format(pred = predictions["model"], diag = predictions["doctor"], advice= predictions["Get second advice"])}
        return render(request,"secondAdvice.html",context = context)
    
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# # Create your views here.
# @api_view(['GET', 'POST'])
# def api_add(request):
#     sum = 0
#     response_dict = {}
#     if request.method == 'GET':
#         # Do nothing
#         pass
#     elif request.method == 'POST':
#         # Add the numbers
#         data = request.data
#         for key in data:
#             sum += data[key]
#         response_dict = {"sum": sum}
#     return Response(response_dict, status=status.HTTP_201_CREATED)