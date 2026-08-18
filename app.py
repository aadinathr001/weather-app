from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/hello", methods=["GET"])
def hello():

    return jsonify({
        "message": "Hello from the weather backend!"
    })


@app.route("/api/weather", methods=["GET"])
def get_weather():

    city = request.args.get("city")

    if not city:
        return jsonify({
            "error": "Please provide a city"
        }), 400


    # -------------------------------
    # Find city coordinates
    # -------------------------------

    geocoding_url = (
        "https://geocoding-api.open-meteo.com/v1/search"
    )

    geocoding_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    geocoding_response = requests.get(
        geocoding_url,
        params=geocoding_params
    )

    if geocoding_response.status_code != 200:

        return jsonify({
            "error": "Could not contact geocoding service"
        }), 500


    geocoding_data = geocoding_response.json()


    if "results" not in geocoding_data:

        return jsonify({
            "error": f"City '{city}' was not found"
        }), 404


    location = geocoding_data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]

    city_name = location["name"]

    country = location.get("country", "")


    # -------------------------------
    # Get weather
    # -------------------------------

    weather_url = (
        "https://api.open-meteo.com/v1/forecast"
    )

    weather_params = {

        "latitude": latitude,

        "longitude": longitude,

        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "weather_code,"
            "wind_speed_10m"
        )
    }

    weather_response = requests.get(
        weather_url,
        params=weather_params
    )


    if weather_response.status_code != 200:

        return jsonify({
            "error": "Could not retrieve weather"
        }), 500


    weather_data = weather_response.json()

    current = weather_data["current"]


    # -------------------------------
    # Prepare response
    # -------------------------------

    result = {

        "city": city_name,

        "country": country,

        "temperature":
            current["temperature_2m"],

        "humidity":
            current["relative_humidity_2m"],

        "wind_speed":
            current["wind_speed_10m"],

        "weather_code":
            current["weather_code"]
    }


    return jsonify(result)


if __name__ == "__main__":

    app.run(debug=True)