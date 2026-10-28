import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pandas as pd
from config import Config
from app.ml.predictor import predict

df = pd.read_csv(Config.PROCCESSED_GAMES_DATA_FILE)

row = df.iloc[630]

pred = predict(row)

print(pred)