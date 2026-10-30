import argparse
import requests
import os
import json
import logging

logging.basicConfig(
         filename="weather.log",
         level=logging.INFO,
         format="%(asctime)s-%(levelname)s-%(message)s"
)

parser=argparse.ArgumentParser()
parser.add_argument("--city")
parser.add_argument("--output")
args=parser.parse_args()

try:
   API_KEY = os.getenv("API_KEY")
   

   params={
     "q": args.city,
     "appid": API_KEY,
     "units": "metric"
   }
   response=requests.get("https://api.openweathermap.org/data/2.5/weather", params=params, timeout=5)
   if response.status_code == 200:
       data = response.json()

       weather_info={
         "temperature": data["main"]["temp"],
         "humidity": data["main"]["humidity"]
       }

       with open(args.output, "w") as file:
          json.dump(weather_info, file)


       logging.info("Weather data saved successfully")

   else:
       logging.error("Weather API request failed: %s", response.status_code)
  
except requests.exceptions.ConnectionError:
   logging.error("Unable to connect. Check your internet connection.")

except requests.exception.TimeOut:
   logging.error("Timed out")
