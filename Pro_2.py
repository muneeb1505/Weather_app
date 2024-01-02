import requests
import json
import pyttsx3

city = input("Enter name of city: \n")
url = f"http://api.weatherapi.com/v1/current.json?key=21ae76010d2f4bf2ab0154907233012&q={city}"
r = requests.get(url)


dc = json.loads(r.text)
wthr = dc["current"]["temp_c"]
engine = pyttsx3.init()
text = f"The current weather in {city} is {wthr} degrees"
engine.say(text)
engine.runAndWait()
