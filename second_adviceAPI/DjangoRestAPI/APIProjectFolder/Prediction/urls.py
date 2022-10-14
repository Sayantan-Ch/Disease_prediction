from django.urls import path
import Prediction.views as views

urlpatterns = [
    path('predict/', views.Disease_Predict.as_view(), name = 'predict'),
    path('secondAdvice/', views.secondAdvice_page),
    path('abc/', views.check_advice),
    path('doctorPage/<str:disease>/', views.recommendDoctor),
]