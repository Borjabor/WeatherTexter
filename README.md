# Weather Forecast WhatsApp Notifier

## Description
This Python script retrieves weather forecast data from the OpenWeatherMap API and sends a WhatsApp message with the forecast. It tells the weather for the next 18 hours, in 3-hour increments, sending temperatures in Celsius and weather conditions.

## Installation
1. Clone the repository.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Set up environment variables for your OpenWeatherMap API key, Twilio auth token, Twilio phone number, and your phone number.

## Usage
Run the `main()` function in the script to get the weather forecast and send it via WhatsApp.
There is no loop to keep the script running as I use the PythonAnywhere service to run it every day at a specific time.
