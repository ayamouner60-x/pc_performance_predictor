from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CPU(db.Model):
    __tablename__ = 'cpus'
    
    id                  = db.Column(db.Integer, primary_key=True)
    name                = db.Column(db.String(100), nullable=False, unique=True)
    cores               = db.Column(db.Integer)
    threads             = db.Column(db.Integer)
    multiplier_unlocked = db.Column(db.Boolean)
    tdp                 = db.Column(db.Integer)
    turbo_clock         = db.Column(db.Float)


class GPU(db.Model):
    __tablename__ = 'gpus'
    
    id                    = db.Column(db.Integer, primary_key=True)
    name                  = db.Column(db.String(100), nullable=False, unique=True)
    architecture          = db.Column(db.String(50))
    boost_clock           = db.Column(db.Float)
    bus_interface         = db.Column(db.String(20))
    die_size              = db.Column(db.Float)
    direct_x              = db.Column(db.String(20))
    vram_gb               = db.Column(db.Integer)
    memory_type           = db.Column(db.String(20))
    pixel_rate            = db.Column(db.Float)
    number_of_rops        = db.Column(db.Integer)
    shader                = db.Column(db.Float)
    texture_rate          = db.Column(db.Float)
    number_of_transistors = db.Column(db.Float)
    vulkan_version        = db.Column(db.String(20))

class Game(db.Model):
    __tablename__ = 'games'
    __table_args__ = (db.UniqueConstraint('name', 'game_setting', name='_game_setting_uc'),)
    
    id             = db.Column(db.Integer, primary_key=True)
    name           = db.Column(db.String(255), nullable=False)
    game_setting   = db.Column(db.String(50), nullable=False)
