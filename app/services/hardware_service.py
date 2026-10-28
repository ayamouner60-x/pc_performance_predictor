import sqlite3
from config import Config

class HardwareService:
    
    def get_cpu_details(cpu_name):
        conn = sqlite3.connect(Config.DB_PATH)
        conn.row_factory = sqlite3.Row
        
        cpu = conn.execute('SELECT * FROM cpus WHERE name = ?', (cpu_name,)).fetchone()
        conn.close()
        
        if cpu:
            return dict(cpu)
        return None
        

    def get_gpu_details(gpu_name):
        conn = sqlite3.connect(Config.DB_PATH)
        conn.row_factory = sqlite3.Row
        
        gpu = conn.execute('SELECT * FROM gpus WHERE name = ?', (gpu_name,)).fetchone()
        conn.close()
        
        if gpu:
            return dict(gpu)
        return None

    def get_all_cpus():
        conn = sqlite3.connect(Config.DB_PATH)
        conn.row_factory = sqlite3.Row
        
        cpus = conn.execute('SELECT name FROM cpus')
        names = [row['name'] for row in cpus]
        conn.close()
        
        return names

    def get_all_gpus():
        conn = sqlite3.connect(Config.DB_PATH)
        conn.row_factory = sqlite3.Row
        
        gpus = conn.execute('SELECT name FROM gpus')
        names = [row['name'] for row in gpus]
        conn.close()
        
        return names
    
    def get_all_games():
        conn = sqlite3.connect(Config.DB_PATH)
        conn.row_factory = sqlite3.Row
        
        games = conn.execute('SELECT DISTINCT name FROM games')
        names = [row['name'] for row in games]
        conn.close()
        
        return names
    
    def get_all_settings():
        conn = sqlite3.connect(Config.DB_PATH)
        conn.row_factory = sqlite3.Row
        
        settings = conn.execute('SELECT DISTINCT game_setting FROM games')
        settings = [row['game_setting'] for row in settings]
        conn.close()
        
        return settings