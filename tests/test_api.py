import requests
import json
import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import Config
from app.services.prediction_service import PredictionService

url = "http://localhost:5000/api/predict"

row = {
    'CpuName': 'Intel Core i9-9900K',
    'GpuName': 'NVIDIA GeForce RTX 2080 Ti',
    'GameName': 'callOfDutyWW2',
    'GameSetting': 'med'
}
response = requests.post(url, json=row)
# response = PredictionService().predict_fps_logic(row)
print(response.json())