import joblib
import pandas as pd
import numpy as np
from config import Config

def load_model_data(model_name="XGB"):
    path = Config.MODEL_PATH.replace(".pkl", f"_{model_name}.pkl")
    return joblib.load(path)

def predict(input_data, model_name="XGB"):
    model_data = load_model_data(model_name)
    model = model_data['model']
    columns_to_drop = model_data['columns_to_drop']

    df = pd.DataFrame([input_data])
    df.drop(columns=columns_to_drop, inplace=True, errors='ignore')
    
    prediction = model.predict(df)
    prediction = np.expm1(prediction)
    return prediction[0]

def dataFramePredict(df, model_name="XGB"):
    model_data = load_model_data(model_name)
    model = model_data['model']
    columns_to_drop = model_data['columns_to_drop']

    df_copy = df.copy()
    df_copy.drop(columns=columns_to_drop, inplace=True, errors='ignore')
    
    prediction = model.predict(df_copy)
    prediction = np.expm1(prediction)
    return prediction

if __name__ == "__main__":
    input_data = {
        'GpuName': 'NVIDIA GeForce RTX 3080',
        'GpuArchitecture': 'Ampere',
        'GpuMemoryType': 'GDDR6X',
        'GpuMemorySize': 10,
        'GpuBus.interface': 'PCIe 4.0 x16',
        'GpuDirectX': '12 Ultimate',
        'GpuVulkan': '1.2.131',
        'CpuName': 'Intel Core i9-10900K',
        'CpuCores': 10,
        'CpuThreads': 20,
        'CpuBoostClock': 5.3,
        'GameName': 'Cyberpunk 2077',
        'GameSetting': 'max'
    }
    
    prediction = predict(input_data, model_name="XGB")
    print(f"Predicted FPS: {prediction}")