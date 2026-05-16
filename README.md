# Smart Crop Recommendation Tool

A Flask web app that recommends the best crop to grow based on real-time weather data and soil nutrient levels.

## How It Works

1. Enter your city and soil values (N, P, K, pH)
2. The app fetches live weather data (temperature, humidity, rainfall) from OpenWeatherMap
3. A trained ML model predicts the most suitable crop for those conditions

## Features

- Live weather integration via OpenWeatherMap API
- Machine learning crop prediction (Random Forest / scikit-learn)
- Displays weather and soil data alongside the recommendation

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/Krrish1k/climate_crop.git
   cd climate_crop
   ```

2. Install dependencies:
   ```bash
   pip install flask requests joblib numpy python-dotenv scikit-learn
   ```

3. Create a `.env` file with your OpenWeatherMap API key:
   ```
   API_KEY=your_openweathermap_api_key
   ```

4. Run the app:
   ```bash
   python bk.py
   ```

5. Open `http://127.0.0.1:5000` in your browser.

## Inputs

| Field      | Description                        |
|------------|------------------------------------|
| City       | Your location (for weather lookup) |
| Nitrogen   | Soil nitrogen content (mg/kg)      |
| Phosphorus | Soil phosphorus content (mg/kg)    |
| Potassium  | Soil potassium content (mg/kg)     |
| pH         | Soil pH level                      |

## Tech Stack

- Python, Flask
- scikit-learn (joblib model)
- OpenWeatherMap API
