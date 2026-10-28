import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pandas as pd
from config import Config
from app.services.hardware_service import HardwareService



def test_get_all_cpus():
    cpus = HardwareService.get_all_cpus()
    print(cpus)

test_get_all_cpus()

def test_get_all_gpus():
    gpus = HardwareService.get_all_gpus()
    print(gpus)

test_get_all_gpus()