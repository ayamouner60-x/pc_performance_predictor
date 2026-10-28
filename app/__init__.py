from flask import Flask

# config
from config import Config

# blueprints
from app.routes.main import main
from app.routes.api import api

# models
from app.models.db_models import db

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    db.init_app(app)
    
    app.register_blueprint(main)
    app.register_blueprint(api)
    
    return app