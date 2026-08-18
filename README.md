# 🌤️ Weather App

A beginner-friendly full-stack weather application built to understand how **frontend, backend, REST APIs, and external APIs communicate with each other**.

The application allows a user to enter a city name and retrieve its current weather information.

## 📌 Project Overview

This project demonstrates the following flow:

```text
Frontend
   ↓
Flask Backend API
   ↓
Open-Meteo Geocoding API
   ↓
Latitude & Longitude
   ↓
Open-Meteo Weather API
   ↓
Flask Backend
   ↓
Frontend
```

The project was intentionally kept simple so that the API communication process can be understood clearly before introducing databases, authentication, or more complex frameworks.

## ✨ Features

* Search weather by city name
* Get current temperature
* Get humidity
* Get wind speed
* Display country and city
* Flask REST API backend
* Frontend built with HTML, CSS, and JavaScript
* Uses Open-Meteo API for weather data
* Error handling for invalid or missing cities

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask
* Requests

### External API

* Open-Meteo Geocoding API
* Open-Meteo Weather API

### Deployment

* GitHub
* Render

## 📂 Project Structure

```text
weather-app/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## 🔄 How the Application Works

When a user enters a city such as:

```text
London
```

the frontend sends a request to the Flask backend:

```http
GET /api/weather?city=London
```

### 1. Flask receives the request

The backend reads the city from the query parameter:

```python
city = request.args.get("city")
```

### 2. Flask calls the Geocoding API

The city name is sent to Open-Meteo to find its coordinates.

For example:

```text
London
↓
Latitude: 51.5085
Longitude: -0.1257
```

### 3. Flask calls the Weather API

The coordinates are then sent to the Open-Meteo weather endpoint.

### 4. Flask prepares the response

The backend extracts the required weather information and returns JSON similar to:

```json
{
    "city": "London",
    "country": "United Kingdom",
    "temperature": 22.5,
    "humidity": 70,
    "wind_speed": 12.4,
    "weather_code": 1
}
```

### 5. Frontend displays the result

JavaScript receives the JSON response and updates the webpage.

## 🔗 API Endpoint

The project provides the following backend endpoint:

### Get Weather

```http
GET /api/weather?city={city_name}
```

Example:

```http
GET /api/weather?city=London
```

Example response:

```json
{
    "city": "London",
    "country": "United Kingdom",
    "temperature": 22.5,
    "humidity": 70,
    "wind_speed": 12.4,
    "weather_code": 1
}
```

## 🚀 Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/weather-app.git
```

Move into the project folder:

```bash
cd weather-app
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

On Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Flask application

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000/
```

## 📡 API Testing

The backend API can also be tested directly in a browser.

Open:

```text
http://127.0.0.1:5000/api/weather?city=London
```

You should receive a JSON response containing the current weather information.

This is useful for understanding that the Flask backend itself is an API, separate from the webpage.

## 🧠 Concepts Learned

This project was created as a practical introduction to:

* What an API is
* Client-server architecture
* HTTP requests and responses
* GET requests
* REST API endpoints
* URL paths
* Query parameters
* JSON data
* Flask routes
* Calling an external API from a backend
* Using Python `requests`
* Returning JSON from Flask
* Connecting frontend JavaScript to a backend API
* Basic error handling
* Hosting a Flask application

## 🔑 Important API Concepts

### GET

Used to retrieve information.

```http
GET /api/weather?city=London
```

### Query Parameter

The part after `?`:

```text
?city=London
```

In Flask:

```python
request.args.get("city")
```

### JSON

A common format for sending structured data between applications.

Example:

```json
{
    "city": "London",
    "temperature": 22.5
}
```

## 🌐 Deployment

The application can be deployed using GitHub and Render.

Typical deployment flow:

```text
Local Project
     ↓
Git
     ↓
GitHub Repository
     ↓
Render
     ↓
Live Web Application
```

## 🔮 Future Improvements

Possible future improvements include:

* 5-day weather forecast
* Weather icons
* Automatic location detection
* Search history
* SQLite database
* Temperature unit selection
* Sunrise and sunset times
* Better mobile UI
* Loading animations
* Weather-based background changes
* User authentication

## 📚 Data Source

Weather and geocoding information are provided by **Open-Meteo**.

* Open-Meteo: https://open-meteo.com/

## 👨‍💻 Author

**Aadinath R**

B.Tech Computer Science and Engineering (AI & ML)

---

⭐ If you found this project useful, consider giving the repository a star!
