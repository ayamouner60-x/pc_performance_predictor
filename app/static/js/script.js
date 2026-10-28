document.addEventListener('DOMContentLoaded', function() {
    AOS.init({
        once: true,
        offset: 50,
    });
    
    loadDropdownOptions();
});

function loadDropdownOptions() {
    Promise.all([
        loadGPUs(),
        loadCPUs(),
        loadGames(),
        loadSettings()
    ]).catch(error => console.error('Error loading dropdown options:', error));
}

function loadGPUs() {
    return fetch('/api/gpus')
        .then(response => response.json())
        .then(data => {
            const select = document.getElementById('gpuInput');
            if (data.success && Array.isArray(data.gpus)) {
                data.gpus.forEach(gpu => {
                    const option = document.createElement('option');
                    option.value = gpu;
                    option.textContent = gpu;
                    select.appendChild(option);
                });
            }
        });
}

function loadCPUs() {
    return fetch('/api/cpus')
        .then(response => response.json())
        .then(data => {
            const select = document.getElementById('cpuInput');
            if (data.success && Array.isArray(data.cpus)) {
                data.cpus.forEach(cpu => {
                    const option = document.createElement('option');
                    option.value = cpu;
                    option.textContent = cpu;
                    select.appendChild(option);
                });
            }
        });
}

function loadGames() {
    return fetch('/api/games')
        .then(response => response.json())
        .then(data => {
            const select = document.getElementById('gameInput');
            if (data.success && Array.isArray(data.games)) {
                data.games.forEach(game => {
                    const option = document.createElement('option');
                    option.value = game;
                    option.textContent = game;
                    select.appendChild(option);
                });
            }
        });
}

function loadSettings() {
    return fetch('/api/settings')
        .then(response => response.json())
        .then(data => {
            const select = document.getElementById('settingsInput');
            if (data.success && Array.isArray(data.settings)) {
                data.settings.forEach(setting => {
                    const option = document.createElement('option');
                    option.value = setting;
                    option.textContent = setting;
                    select.appendChild(option);
                });
            }
        });
}

function predictFPS() {
    const gpu = document.getElementById('gpuInput').value.trim();
    const cpu = document.getElementById('cpuInput').value.trim();
    const game = document.getElementById('gameInput').value.trim();
    const settings = document.getElementById('settingsInput').value.trim();
    
    // الجزء الجديد: سحب نوع الموديل من الـ HTML
    const model = document.getElementById('modelInput').value;

    const resultArea = document.getElementById('resultArea');
    const fpsValue = document.getElementById('fpsValue');
    const systemSummary = document.getElementById('systemSummary');

    if(!gpu || !cpu || !game || !settings) {
        alert("Please fill in all fields!");
        return;
    }

    resultArea.classList.remove('hidden');
    setTimeout(() => {
        resultArea.classList.remove('translate-y-4', 'opacity-0');
        resultArea.classList.add('opacity-100', 'translate-y-0');
    }, 50);

    fpsValue.innerText = "Calculating...";
    fpsValue.classList.replace('text-accentBlue', 'text-textMuted');
    systemSummary.innerText = "";

    fetch('/api/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            CpuName: cpu,
            GpuName: gpu,
            GameName: game,
            GameSetting: settings,
            model_type: model // إرسال نوع الموديل المختار
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            fpsValue.classList.replace('text-textMuted', 'text-accentBlue');
            fpsValue.innerText = data.fps + " FPS";
            // تحديث الرسالة لتشمل اسم الموديل المستخدم في التوقع
            systemSummary.innerText = `Predicted using ${data.model_used} engine on ${settings} settings.`;
        } else {
            fpsValue.classList.replace('text-textMuted', 'text-accentBlue');
            fpsValue.innerText = "Error";
            systemSummary.innerText = data.error || "Prediction failed.";
        }
    })
    .catch(error => {
        fpsValue.classList.replace('text-textMuted', 'text-accentBlue');
        fpsValue.innerText = "Error";
        systemSummary.innerText = "Network error. Please try again.";
        console.error('API Error:', error);
    });
}