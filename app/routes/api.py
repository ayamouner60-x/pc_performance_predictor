from flask import Blueprint, request
from app.services.prediction_service import PredictionService
from app.services.hardware_service import HardwareService

api = Blueprint('api', __name__)

@api.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    pred = PredictionService()
    response = pred.predict_fps_logic(data)
    return response

@api.route('/api/cpus', methods=['GET'])
def get_cpus():
    cpus = HardwareService.get_all_cpus()
    return {'success': True, 'cpus': cpus}

@api.route('/api/gpus', methods=['GET'])
def get_gpus():
    gpus = HardwareService.get_all_gpus()
    return {'success': True, 'gpus': gpus}

@api.route('/api/games', methods=['GET'])
def get_games():
    games = HardwareService.get_all_games()
    return {'success': True, 'games': games}

@api.route('/api/settings', methods=['GET'])
def get_settings():
    settings = HardwareService.get_all_settings()
    return {'success': True, 'settings': settings}
