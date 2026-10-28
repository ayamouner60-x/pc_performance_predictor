# PC-Performance-Predictor

An AI-powered system to analyze hardware specifications and predict gaming performance (FPS) with high accuracy.

## 📋 Overview

PC-Performance-Predictor is a Flask-based web application that uses machine learning to predict Frames Per Second (FPS) for games based on hardware specifications. Simply input your CPU, GPU, game name, and graphics settings to get an accurate FPS prediction.

## ✨ Features

- **AI-Powered Predictions**: Machine learning model trained on real gaming data
- **Hardware Database**: Comprehensive database of CPU and GPU specifications
- **Beautiful UI**: Modern, responsive interface with smooth animations
- **Real-time API**: RESTful API for programmatic access
- **Data Processing**: Automated data cleaning and preprocessing pipeline
- **Model Training**: Jupyter notebooks for model exploration and training

## 🚀 Installation

### Prerequisites

- Python 3.8+
- pip or conda

### Setup

1. Clone the repository:

```bash
git clone https://github.com/aliosama/PC-Performance-Predictor.git
cd PC-Performance-Predictor
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python run.py
```

The application will be available at `http://localhost:5000`

## 📁 Project Structure

```
PC-Performance-Predictor/
├── app/
│   ├── ml/                 # Machine learning models and training
│   │   ├── predictor.py    # Prediction logic
│   │   └── train.py        # Model training script
│   ├── models/             # Database models
│   │   └── db_models.py
│   ├── routes/             # Flask routes
│   │   ├── api.py          # REST API endpoints
│   │   └── main.py         # Main application routes
│   ├── services/           # Business logic
│   │   ├── hardware_service.py
│   │   └── prediction_service.py
│   ├── templates/          # HTML templates
│   │   ├── base.html       # Base template
│   │   ├── dashBoard.html  # DashBoard
│   │   └── index.html      # Home page
│   └── static/             # Static files (CSS, JS)
│       ├── css/
│       └── js/
├── data/                   # Data files
│   ├── raw/                # Original datasets
│   ├── processed/          # Processed datasets
│   └── seed.py             # Database seeding
├── notebooks/              # Jupyter notebooks
│   ├── Cleaning_Games_Data.ipynb
│   └── Games_Data_Model.ipynb
├── tests/                  # Unit tests
├── config.py               # Configuration settings
└── run.py                  # Application entry point
```

## 🔌 API Documentation

### Predict FPS Endpoint

**POST** `/api/predict`

Request body:

```json
{
  "CpuName": "Intel Core i9-9900K",
  "GpuName": "NVIDIA GeForce RTX 2080 Ti",
  "GameName": "callOfDutyWW2",
  "GameSetting": "med"
}
```

Response:

```json
{
  "success": true,
  "fps": 85.5
}
```

Error response:

```json
{
  "success": false,
  "error": "Hardware not found"
}
```

## 📊 Data

The project includes:

- **FPS_Games.csv**: Raw gaming performance dataset
- **FPS_Games_Processed.csv**: Cleaned and processed dataset

See `notebooks/` for data exploration and model training workflows.

## 🔧 Configuration

Edit `config.py` to customize:

- Database settings
- Model parameters
- API configuration

## 👤 Author

Created by Ali Osama

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
