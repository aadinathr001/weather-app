from flask import Flask, jsonify, request, render_template
import requests
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

app = Flask(__name__)

# Get WeatherAPI key from environment variable
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------------------------
# TEST API
# --------------------------------------------------

@app.route("/api/hello", methods=["GET"])
def hello():

    return jsonify({
        "message": "Hello from the weather backend!"
    })


# --------------------------------------------------
# WEATHER API
# --------------------------------------------------

@app.route("/api/weather", methods=["GET"])
def get_weather():

    # ----------------------------------------------
    # 1. Get city from our URL
    #
    # Example:
    # /api/weather?city=London
    # ----------------------------------------------

    city = request.args.get("city")

    if not city:
        return jsonify({
            "error": "Please provide a city"
        }), 400


    # ----------------------------------------------
    # 2. Check whether API key exists
    # ----------------------------------------------

    if not WEATHER_API_KEY:

        return jsonify({
            "error": "Weather API key is not configured"
        }), 500


    # ----------------------------------------------
    # 3. Prepare parameters for WeatherAPI
    # ----------------------------------------------

    params = {
        "key": WEATHER_API_KEY,
        "q": city,
        "aqi": "no"
    }


    # ----------------------------------------------
    # 4. Send request to WeatherAPI
    # ----------------------------------------------

    try:

        response = requests.get(
            WEATHER_API_URL,
            params=params,
            timeout=10
        )

    except requests.RequestException:

        return jsonify({
            "error": "Could not connect to WeatherAPI"
        }), 502


    # ----------------------------------------------
    # 5. Handle errors from WeatherAPI
    # ----------------------------------------------

    if response.status_code != 200:

        try:
            error_data = response.json()
        except ValueError:
            error_data = {}

        error_message = (
            error_data
            .get("error", {})
            .get("message", "Weather service returned an error")
        )

        return jsonify({
            "error": error_message
        }), response.status_code


    # ----------------------------------------------
    # 6. Convert JSON into Python dictionary
    # ----------------------------------------------

    weather_data = response.json()


    # ----------------------------------------------
    # 7. Extract the data we need
    # ----------------------------------------------

    location = weather_data["location"]
    current = weather_data["current"]


    result = {

        "city": location["name"],

        "country": location["country"],

        "temperature": current["temp_c"],

        "humidity": current["humidity"],

        "wind_speed": current["wind_kph"],

        "condition": current["condition"]["text"],

        "icon": current["condition"]["icon"],

        "feels_like": current["feelslike_c"],

        "uv": current["uv"]
    }


    # ----------------------------------------------
    # 8. Send our own JSON response
    # ----------------------------------------------

    return jsonify(result)


# --------------------------------------------------
# START SERVER
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)