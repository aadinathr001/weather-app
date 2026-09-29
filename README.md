# 🌤️ Weather App

A responsive, full-stack weather application built with **Python, Flask, HTML, CSS, and JavaScript**. Search for any city and view its current weather conditions using the [WeatherAPI.com](https://www.weatherapi.com/) API.

<p align="center">
  <a href="https://weather-app-gtvc.onrender.com/">
    <strong>🌐 Live Demo</strong>
  </a>
  &nbsp; • &nbsp;
  <a href="https://github.com/aadinathr001/weather-app">
    <strong>📂 GitHub Repository</strong>
  </a>
</p>

---

## 📌 About the Project

The Weather App is a web application that allows users to search for a city and retrieve its current weather information.

The project uses **Flask as the backend**, which communicates with WeatherAPI.com to fetch weather data. The frontend is built using HTML, CSS and JavaScript to provide an interactive interface and display the retrieved information.

This project demonstrates the practical use of REST APIs, backend development, frontend integration, environment variables and web application deployment.

## ✨ Features

* 🔍 **City Search:** Search for current weather conditions by entering a city name.
* 🌡️ **Temperature:** View the current temperature in Celsius.
* 🌤️ **Weather Conditions:** See a description of the current weather, such as sunny or cloudy.
* 💧 **Humidity:** View the current relative humidity.
* 💨 **Wind Speed:** Check the current wind speed.
* 🌡️ **Feels Like:** View the apparent temperature.
* ☀️ **UV Index:** Check the current UV index.
* 🌍 **Location Information:** Display the searched city's name and country.
* 🖼️ **Weather Icons:** Display visual icons corresponding to weather conditions.
* 📱 **Responsive Design:** Use the application on desktop and mobile browsers.
* 🔐 **Secure API Key Handling:** Keep the API key on the backend using an environment variable.
* ⚠️ **Error Handling:** Handle unsuccessful searches and API errors.

## 🌐 Live Demo

**[Visit the Weather App →](https://weather-app-gtvc.onrender.com/)**

Try searching for:

* London
* Tokyo
* New York
* Thiruvananthapuram
* Mumbai

*Note: The application is hosted on Render. If it is using a free web service, it may take a short time to respond after a period of inactivity.*

---

## 🖥️ Screenshots

<!-- Add screenshots of your actual application here.
     Upload the images to your repository first. -->

<!-- Example:
![Weather App Screenshot](screenshots/weather-app.png)
-->

---

## 🛠️ Tech Stack

| Technology     | Purpose                                                   |
| -------------- | --------------------------------------------------------- |
| Python         | Backend programming                                       |
| Flask          | Backend web framework and API routes                      |
| HTML5          | Webpage structure                                         |
| CSS3           | Styling and responsive design                             |
| JavaScript     | Frontend interaction and dynamic updates                  |
| Requests       | Sending HTTP requests to the weather API                  |
| WeatherAPI.com | Current weather data provider                             |
| python-dotenv  | Loading environment variables from a `.env` file, if used |
| Git & GitHub   | Version control and source code hosting                   |
| Render         | Web application hosting                                   |

---

## 🏗️ Application Architecture

The application follows a client-server architecture.

```text
                USER
                  |
                  v
          FRONTEND INTERFACE
           HTML / CSS / JS
                  |
                  | City search
                  v
           FLASK BACKEND
                  |
                  | HTTP GET request
                  v
           WEATHERAPI.COM
                  |
                  | JSON response
                  v
           FLASK BACKEND
                  |
                  | Process weather data
                  v
          JSON RESPONSE
                  |
                  v
          JAVASCRIPT FRONTEND
                  |
                  v
          DISPLAY WEATHER DATA
```

### How It Works

1. The user enters a city name in the search field.
2. JavaScript sends a request to the Flask backend.
3. The Flask backend retrieves the API key from an environment variable.
4. The backend sends a request to WeatherAPI.com with the city name and API key.
5. WeatherAPI.com returns the requested weather information in JSON format.
6. Flask processes the response and sends the relevant information to the frontend.
7. JavaScript updates the webpage to display the weather conditions.

---

## 📂 Project Structure

```text
weather-app/
│
├── app.py
│
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── .env
├── .gitignore
└── README.md
```

| File / Folder          | Description                                                        |
| ---------------------- | ------------------------------------------------------------------ |
| `app.py`               | Main Flask application, backend routes and weather API integration |
| `requirements.txt`     | List of required Python packages                                   |
| `templates/`           | Contains the HTML template                                         |
| `templates/index.html` | Main application webpage                                           |
| `static/`              | Contains frontend static files                                     |
| `static/style.css`     | Styles and layout for the application                              |
| `static/script.js`     | Handles user interactions and dynamic weather updates              |
| `.env`                 | Stores the API key locally, if using a dotenv setup                |
| `.gitignore`           | Excludes sensitive files and unnecessary files from Git            |
| `README.md`            | Project documentation                                              |

---

## 🚀 Getting Started

Follow these instructions to run the project on your local machine.

### Prerequisites

Before starting, make sure you have installed:

* Python 3
* Git
* A code editor such as Visual Studio Code
* An internet connection

### 1. Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/aadinathr001/weather-app.git
```

Navigate to the project directory:

```bash
cd weather-app
```

### 2. Create a Virtual Environment

A virtual environment keeps the dependencies of this project separate from other Python projects.

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows (Command Prompt):**

```cmd
.venv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

Once activated, you should see the environment name in your terminal.

### 4. Install Dependencies

Install the packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Configure the API Key

This application requires an API key from WeatherAPI.com.

1. Visit [WeatherAPI.com](https://www.weatherapi.com/).
2. Create an account and obtain your API key.
3. Create a `.env` file in the root directory of your project if your application uses `python-dotenv`.
4. Add your API key:

```env
WEATHER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

**Important:** Never upload your actual API key to a public GitHub repository. Add `.env` to your `.gitignore` file.

If your existing application uses environment variables directly instead of `python-dotenv`, set the variable in your terminal or hosting service instead of creating a `.env` file.

### 6. Run the Application

Start the Flask development server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

You should now be able to search for a city and view its current weather information.

---

## 🔗 API Integration

This project uses [WeatherAPI.com](https://www.weatherapi.com/) to retrieve current weather information.

### Current Weather Endpoint

**API endpoint:**

```http
https://api.weatherapi.com/v1/current.json
```

The backend sends a request using the following query parameters:

| Parameter | Description                                          |
| --------- | ---------------------------------------------------- |
| `key`     | API key used to authenticate the request             |
| `q`       | City name or other supported location identifier     |
| `aqi`     | Controls whether air quality information is included |

### Example API Request

```http
GET https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=London&aqi=no
```

### Weather Information

The application retrieves information such as:

| Field                    | Description                       |
| ------------------------ | --------------------------------- |
| `location.name`          | City name                         |
| `location.country`       | Country                           |
| `current.temp_c`         | Current temperature in Celsius    |
| `current.feelslike_c`    | Feels-like temperature in Celsius |
| `current.humidity`       | Relative humidity percentage      |
| `current.wind_kph`       | Wind speed in kilometres per hour |
| `current.condition.text` | Weather condition description     |
| `current.condition.icon` | Weather icon URL                  |
| `current.uv`             | UV index                          |

For more information, refer to the [WeatherAPI.com documentation](https://www.weatherapi.com/docs/).

---

## 🔌 Backend API

The Flask backend provides an endpoint for retrieving weather information based on the requested city.

### Get Weather by City

**Method:** `GET`

**Endpoint:**

```http
/api/weather?city={city_name}
```

**Example:**

```http
/api/weather?city=London
```

The backend retrieves the weather information from WeatherAPI.com and returns a JSON response to the frontend.

### Example Response

The following is an illustrative example of the data that a frontend weather application might receive. Your exact response keys and structure depend on the implementation in `app.py`.

```json
{
  "city": "London",
  "country": "United Kingdom",
  "temperature": 18.5,
  "feels_like": 18.2,
  "humidity": 65,
  "wind_speed": 12.6,
  "condition": "Partly cloudy",
  "icon": "//cdn.weatherapi.com/weather/...",
  "uv": 3
}
```

### Error Handling

The application should handle common errors such as:

* Empty city search
* Invalid or unrecognized city
* Failed connection to the external weather service
* Invalid or missing API key
* API rate limits or service errors

The frontend can display an appropriate error message when a request fails.

---

## ☁️ Deployment

The application is hosted on **Render**, which supports deploying web applications directly from a GitHub repository.

### Deployment Workflow

1. Push the project code to GitHub.
2. Create a web service in Render.
3. Connect the GitHub repository.
4. Configure the Python environment and build command.
5. Configure the application start command.
6. Add `WEATHER_API_KEY` as an environment variable in Render.
7. Deploy the application and access the public URL.

**Live application:** https://weather-app-gtvc.onrender.com/

### Environment Variables on Render

For secure deployment, configure the API key in the Render dashboard rather than committing it to your source code.

Set the environment variable:

```text
WEATHER_API_KEY
```

Use your actual API key as its value.

---

## 🧠 Key Concepts Learned

Developing this project provided practical experience with:

* **Backend Development:** Creating a web application using Flask.
* **REST API Integration:** Sending HTTP requests to an external weather service.
* **JSON Processing:** Retrieving and processing JSON responses.
* **Frontend-Backend Communication:** Connecting JavaScript with a Python backend.
* **Dynamic Web Pages:** Updating the interface based on user input and API responses.
* **Environment Variables:** Keeping API credentials outside the source code.
* **Error Handling:** Managing failed requests and unexpected API responses.
* **Virtual Environments:** Managing isolated Python dependencies.
* **Deployment:** Hosting a full-stack application on Render.
* **Version Control:** Using Git and GitHub to manage and publish source code.

---

## 🔮 Future Improvements

Possible enhancements for future versions include:

* 🌦️ **Multi-Day Forecast:** Display weather forecasts for upcoming days.
* 🕒 **Hourly Forecast:** Show changes in weather throughout the day.
* 📍 **Geolocation:** Automatically retrieve the weather for the user's current location.
* 🌡️ **Temperature Conversion:** Switch between Celsius and Fahrenheit.
* 🌅 **Sunrise and Sunset:** Display daily sunrise and sunset times.
* 🕘 **Search History:** Save recently searched cities.
* 📊 **Weather Charts:** Visualize temperature and other weather trends.
* 🎨 **Dynamic Themes:** Change the interface based on weather conditions.
* ⏳ **Improved Loading States:** Add loading animations while retrieving weather data.

---

## 🔐 Security Considerations

* Keep the API key in an environment variable rather than hardcoding it in the source code.
* Never commit `.env` files containing credentials.
* Configure the API key in the deployment platform's environment settings.
* Handle external API errors without exposing sensitive configuration details.
* Avoid sending the private API key directly to the browser.

---

## 👨‍💻 Author

**Aadinath R**

B.Tech in Computer Science and Engineering (AI & ML)

* **GitHub:** [@aadinathr001](https://github.com/aadinathr001)
* **Project Repository:** [Weather App](https://github.com/aadinathr001/weather-app)
* **Live Demo:** [Weather App on Render](https://weather-app-gtvc.onrender.com/)

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a star on GitHub!
