from app.services.hardware_service import HardwareService
from app.ml.predictor import predict

class PredictionService:
    def predict_fps_logic(self, data:dict):
        model_name = data.get('model_type', 'XGB') 
        cpu_name = data.get('CpuName')
        gpu_name = data.get('GpuName')
        game_name = data.get('GameName')
        game_setting = data.get('GameSetting')

        # جلب تفاصيل الهاردوير من قاعدة البيانات
        cpu_info = HardwareService.get_cpu_details(cpu_name)
        gpu_info = HardwareService.get_gpu_details(gpu_name)

        if not cpu_info or not gpu_info:
            return {"success": False, "error": "Hardware not found in database"}

        # بناء الـ Dictionary بنفس مفاتيح (Keys) كود الـ Predict اللي أنت بعته
        full_input = {
            'GpuName': gpu_name,
            'GpuArchitecture': gpu_info['architecture'],
            'GpuMemoryType': gpu_info['memory_type'],
            'GpuMemorySize': gpu_info['vram_gb'],
            'GpuBus.interface': gpu_info['bus_interface'],
            'GpuDirectX': gpu_info['direct_x'],
            'GpuVulkan': gpu_info['vulkan_version'],
            'CpuName': cpu_name,
            'CpuCores': cpu_info['cores'],
            'CpuThreads': cpu_info['threads'],
            'CpuBoostClock': cpu_info['turbo_clock'],
            'GameName': game_name,
            'GameSetting': game_setting
        }

        try:
            # استدعاء فانكشن الـ predict من ملف الـ predictor
            prediction = predict(full_input, model_name=model_name)
            
            return {
                "success": True,
                "fps": round(float(prediction), 2),
                "model_used": model_name
            }
        except Exception as e:
            # طباعة الخطأ في السيرفر للديناج
            print(f"Error during prediction: {str(e)}")
            return {"success": False, "error": f"Model Error: {str(e)}"}