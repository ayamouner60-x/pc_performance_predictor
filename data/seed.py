import pandas as pd
import sys
sys.path.append('.')
from app import create_app
from app.models.db_models import db, CPU, GPU, Game

def seed_database():
    app = create_app()
    
    with app.app_context():
        db.create_all()
        
        df = pd.read_csv('data/processed/FPS_Games_Processed.csv')
        
        for _, row in df.iterrows():
            cpu = CPU.query.filter_by(name=row['CpuName']).first()
            if not cpu:
                cpu = CPU(
                    name=row['CpuName'],
                    cores=row['CpuNumberOfCores'],
                    threads=row['CpuNumberOfThreads'],
                    multiplier_unlocked=row['CpuMultiplierUnlocked'],
                    tdp=row['CpuTDP'],
                    turbo_clock=row['CpuTurboClock']
                )
                db.session.add(cpu)
                db.session.flush()
            
            gpu = GPU.query.filter_by(name=row['GpuName']).first()
            if not gpu:
                gpu = GPU(
                    name=row['GpuName'],
                    architecture=row['GpuArchitecture'],
                    boost_clock=row['GpuBoostClock'],
                    bus_interface=row['GpuBus.interface'],
                    die_size=row['GpuDieSize'],
                    direct_x=row['GpuDirectX'],
                    vram_gb=row['GpuMemorySize'],
                    memory_type=row['GpuMemoryType'],
                    pixel_rate=row['GpuPixelRate'],
                    number_of_rops=row['GpuNumberOfROPs'],
                    shader=row['GpuShaderModel'],
                    texture_rate=row['GpuTextureRate'],
                    number_of_transistors=row['GpuNumberOfTransistors'],
                    vulkan_version=row['GpuVulkan']
                )
                db.session.add(gpu)
                db.session.flush()

            game = Game.query.filter_by(name=row['GameName'], game_setting=row['GameSetting']).first()
            if not game:
                game = Game(
                    name=row['GameName'],
                    game_setting=row['GameSetting'],
                )
                db.session.add(game)
                db.session.flush()
        
        db.session.commit()
        print("Database seeded successfully")

if __name__ == '__main__':
    seed_database()