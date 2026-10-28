import sys
sys.path.append('./.')
from config import Config
import joblib
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer, PolynomialFeatures, MinMaxScaler, OneHotEncoder, OrdinalEncoder

def prepare_data_and_preprocessor(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
    X = df.drop('FPS', axis=1)
    y = df['FPS']
    
    log_transformer = FunctionTransformer(func=np.log1p, inverse_func=np.expm1)
    y = log_transformer.fit_transform(y)
    
    columns_to_drop = ['GpuName', 'CpuName']
    numeric_columns = X.select_dtypes(include=np.number).columns
    label_columns = ['GpuBus.interface', 'GpuDirectX', 'GpuVulkan', 'GameSetting']
    one_hot_columns = ['GpuArchitecture', 'GpuMemoryType', 'GameName']
    
    X.drop(columns=columns_to_drop, inplace=True)
    
    ordinal_cat = {
        'GpuBus.interface': ['PCIe 3.0 x16', 'PCIe 4.0 x16'],
        'GpuDirectX': ['12 Ultimate', '12'],
        'GpuVulkan': ['1.2.131', '1.1.126'],
        'GameSetting': ['med', 'max']
    }
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('label', OrdinalEncoder(categories=[ordinal_cat[col] for col in label_columns], handle_unknown='use_encoded_value', unknown_value=-1), label_columns),
            ('onehot', OneHotEncoder(drop='first', sparse_output=False), one_hot_columns),
            ('num', MinMaxScaler(), numeric_columns)
        ],
        remainder='passthrough'
    )
    
    return X, y, preprocessor, numeric_columns, label_columns, one_hot_columns, columns_to_drop


def save_trained_model(trainer, name, MODEL_PATH, numeric_columns, label_columns, one_hot_columns, columns_to_drop):
    current_path = MODEL_PATH.replace(".pkl", f"_{name}.pkl")
    joblib.dump({
        'model': trainer,
        'numeric_columns': numeric_columns,
        'label_columns': label_columns,
        'one_hot_columns': one_hot_columns,
        'columns_to_drop': columns_to_drop,
        'feature_names': trainer.named_steps['preprocessor'].get_feature_names_out()
    }, current_path)
    print(f"Model {name} trained and saved.")



def train_lr_model(DATA_PATH, MODEL_PATH):
    X, y, preprocessor, nc, lc, ohc, cd = prepare_data_and_preprocessor(DATA_PATH)
    trainer = Pipeline([
        ('preprocessor', preprocessor),
        ('poly', PolynomialFeatures(degree=2, include_bias=False)),
        ('model', LinearRegression())
    ])
    trainer.fit(X, y)
    save_trained_model(trainer, "LR", MODEL_PATH, nc, lc, ohc, cd)

def train_xgb_model(DATA_PATH, MODEL_PATH):
    X, y, preprocessor, nc, lc, ohc, cd = prepare_data_and_preprocessor(DATA_PATH)
    trainer = Pipeline([
        ('preprocessor', preprocessor),
        ('model', XGBRegressor( n_estimators=400,
        max_depth=6,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8))])
    
    trainer.fit(X, y)
    save_trained_model(trainer, "XGB", MODEL_PATH, nc, lc, ohc, cd)

def train_rf_model(DATA_PATH, MODEL_PATH):
    X, y, preprocessor, nc, lc, ohc, cd = prepare_data_and_preprocessor(DATA_PATH)
    trainer = Pipeline([
        ('preprocessor', preprocessor),
        ('model', RandomForestRegressor(n_estimators=400,
        max_depth=15,
        min_samples_split=5))
    ])
    trainer.fit(X, y)
    save_trained_model(trainer, "RF", MODEL_PATH, nc, lc, ohc, cd)

if __name__ == '__main__':
    train_lr_model(Config.PROCCESSED_GAMES_DATA_FILE, Config.MODEL_PATH)
    train_xgb_model(Config.PROCCESSED_GAMES_DATA_FILE, Config.MODEL_PATH)
    train_rf_model(Config.PROCCESSED_GAMES_DATA_FILE, Config.MODEL_PATH)