from flask import Flask, render_template, request
import requests
import joblib
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")



model = joblib.load(open("crop_model.joblib", "rb"))
le = joblib.load(open("label_encoder.joblib","rb"))

app = Flask(__name__)

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()
    print(res)

    if "main" not in res:
        return None

    weather = {
        "temp": res["main"]["temp"],
        "humidity": res["main"]["humidity"],
        "rainfall": res.get("rain", {}).get("1h", 0), 
        "lat": res["coord"]["lat"],
        "lon": res["coord"]["lon"]
    }
    return weather

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    city = request.form["city"]
    nitrogen = float(request.form["nitrogen"])
    phosphorus = float(request.form["phosphorus"])
    potassium = float(request.form["potassium"])
    ph = float(request.form["ph"])

    weather = get_weather_data(city)
    if not weather:
        return render_template("index.html", prediction="Invalid city. Try again.")
    features = np.array([[
        nitrogen,                
        phosphorus,              
        potassium,               
        weather["temp"],         
        weather["humidity"],     
        ph,                      
        weather["rainfall"]    
    ]])

    prediction = model.predict(features)[0]
    out = le.inverse_transform([prediction])[0]

    return render_template("index.html",
                           prediction=f"Recommended Crop: {out}",
                           city=city,
                           weather=weather,
                           soil={"nitrogen": nitrogen, "phosphorus": phosphorus, "potassium": potassium, "ph": ph})

if __name__ == "__main__":
    app.run(debug=True)
