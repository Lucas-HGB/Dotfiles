#/usr/bin/env python3

import requests, json
import emoji

WEATHER_REPORTS = {
"mist": "cloud",
"sunny": "\u2600",
"cloud sunny": "\u26C5",
"cloud with lightning and rain": "\u26C8"
}

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

CITY = "3469968"
API_KEY = "63dcfa0ee8a7e6b6be58dd2ff5865e46"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY


response = requests.get(URL)

if response.status_code == 200:
	data = response.json()["main"]

	temperature = data['temp']
	report = data['weather']


	weather_icon = WEATHER_REPORTS.get(report, "ERROR")
	if weather_icon == "ERROR":
		print(report)
	else:
		print(f"{weather_icon}{temperature}°")
else:
   # showing the error message
   print("Error in the HTTP request")