from django.apps import AppConfig
import pandas as pd
from joblib import load
import os

class PredictionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Prediction'
    #CLASSIFIER_FOLDER = Path("classifier")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CLASSIFIER_FOLDER = os.path.join(BASE_DIR, 'Prediction/classifier/')
    #CLASSIFIER_FILE = CLASSIFIER_FOLDER / "disease_predictor.joblib"
    CLASSIFIER_FILE = os.path.join(CLASSIFIER_FOLDER, "disease_predictor.joblib")
    classifier = load(CLASSIFIER_FILE)
