async function getWeather() {

    const cityInput = document.getElementById("cityInput");

    const city = cityInput.value.trim();


    if (city === "") {

        document.getElementById("message").textContent =
            "Please enter a city.";

        return;
    }


    document.getElementById("message").textContent =
        "Loading...";


    const url =
        "/api/weather?city=" +
        encodeURIComponent(city);


    try {

        const response = await fetch(url);

        const data = await response.json();


        if (!response.ok) {

            document.getElementById("message").textContent =
                data.error || "Something went wrong.";

            return;
        }


        document.getElementById("city").textContent =
            `${data.city}, ${data.country}`;

        document.getElementById("temperature").textContent =
            data.temperature;

        document.getElementById("humidity").textContent =
            data.humidity;

        document.getElementById("wind").textContent =
            data.wind_speed;


        document.getElementById("message").textContent = "";

    }

    catch (error) {

        console.error(error);

        document.getElementById("message").textContent =
            "Could not connect to the server.";
    }
}