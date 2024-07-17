This was an exploration in using two different APIs. by doing something I found useful for myself.
The first, was OpenWeather's API, to get a forecast for the day, and save the temperatures and weather conditions in 3 hour increments.
Second, I used Twilio's API to send the forecast information to myself as a WhatsApp message. I left the SMS code as well if preferred.

I had some issues with getting the correct time. I was sending the hours from OpenWeather's timezone at first. 
But I managed to fix it by accessing a different variable and converting using datetime.fromtimestamp().
Not entirely sure it is properly converting, as I'd need to run this code from a different timezone to be certain.
