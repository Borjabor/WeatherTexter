import requests
import os
from twilio.rest import Client
from datetime import datetime

def main():
  """
  Retrieves weather forecast data from the OpenWeatherMap API and sends a WhatsApp message with the forecast.
  Tell the weather for the next 18 hours, in 3 hours increments, sending temperatures in Celsius, and weather conditions.
  
  Replace auth_token and account_sid with your Twilio auth token and account SID, 
  api_key with your OpenWeatherMap API key, 
  my_number with your phone number, 
  and twilio_number with the phone number generated on your Twilio account.

  Returns:
      None.
  """
  
  account_sid = "YourAccountSID"
  auth_token = os.environ.get("TWILIO_AUTH")
  client = Client(account_sid, auth_token)

  OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
  api_key = os.environ.get("OWM_API_KEY")

  my_number = os.environ.get("MY_NUMBER")
  twilio_number = "TwilioGeneratedNumber"

  #Coordinates for your city, you can get them on latlong.net
  parameters = {
      "lat": "YourLat",
      "lon": "YourLon",
      "appid": api_key,
      "cnt": 6
  }

  response = requests.get(OWM_Endpoint, params=parameters)
  response.raise_for_status()
  data = response.json()
  
  hours = [datetime.fromtimestamp(i["dt"]).hour for i in data["list"]]
  temperatures = [round(i["main"]["temp"] - 273, 1) for i in data["list"]]
  conditions = [i["weather"][0]["description"] for i in data["list"]]
      
  forecast = [{hour:{"temperature":temp, "condition":desc}} for hour, temp, desc in zip(hours, temperatures, conditions)]

  message = "Today's forecast: \n"
  for hour in forecast:
      for key, value in hour.items():
          message += f"{key}h - {value['temperature']}°C,\n     Condition: {value['condition']} \n"
          
  whatsapp_message = client.messages.create(
    from_=f"whatsapp:{twilio_number}",
    body=message,
    to=f"whatsapp:{my_number}"
  )
  
  #use the code below instead if you want to send the message via SMS. Comment out the code above
  
  # sms_message = client.messages.create(
  #   from_=f"{twilio_number}",
  #   body=message,
  #   to=f"{my_number}"
  # )
  
main()