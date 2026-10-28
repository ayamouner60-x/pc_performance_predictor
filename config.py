import os

class Config:
    """
    Base configuration
    """
    SECRET_KEY = 'FacultyOfAI'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
    DATA_DIR = os.path.join(PROJECT_DIR, 'data')

    RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
    PROCCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

    RAW_GAMES_DATA_FILE = os.path.join(RAW_DATA_DIR, 'FPS_Games.csv')
    PROCCESSED_GAMES_DATA_FILE = os.path.join(PROCCESSED_DATA_DIR, 'FPS_Games_Processed.csv')
    
    DB_PATH = os.path.join(PROJECT_DIR, 'instance', 'database.db')
    
    MODEL_PATH = os.path.join(PROJECT_DIR, 'models', 'fps_games_model.pkl')
