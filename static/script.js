async function getWeather() {

    // --------------------------------------------
    // 1. Get city from input box
    // --------------------------------------------

    const cityInput = document.getElementById("cityInput");

    const city = cityInput.value.trim();


    // --------------------------------------------
    // 2. Check whether user entered a city
    // --------------------------------------------

    if (city === "") {

        document.getElementById("message").textContent =
            "Please enter a city.";

        return;
    }


    // Show loading message

    document.getElementById("message").textContent =
        "Loading...";


    // --------------------------------------------
    // 3. Call our Flask backend
    // --------------------------------------------

    const url =
    "/api/weather?city=" +
    encodeURIComponent(city);


    try {

        const response = await fetch(url);


        // ----------------------------------------
        // 4. Convert response JSON into JS object
        // ----------------------------------------

        const data = await response.json();


        // ----------------------------------------
        // 5. Check for errors
        // ----------------------------------------

        if (!response.ok) {

            document.getElementById("message").textContent =
                data.error || "Something went wrong.";

            return;
        }


        // ----------------------------------------
        // 6. Display data
        // ----------------------------------------

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