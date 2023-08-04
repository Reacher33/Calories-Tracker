import os
import requests
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
shetty_endpoint = "https://api.sheety.co/c5b39e70f5b60e2a6e395a6ab60b44cf/copyOfMyWorkouts/workouts"
today = datetime.now()

shetty_header = {"Authorization": os.environ.get("SHETTY_AUTH")}
headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}
params = {"query": input("What were your activities today? ")}

response = requests.post(url=exercise_endpoint,  json=params, headers=headers)
data = response.json()["exercises"]
new_data = [items for items in data][0]

DURATION = new_data["duration_min"]
CALORIES = new_data["nf_calories"]
EXERCISE = new_data["name"]
EXERCISE = EXERCISE.title()
DATE = today.strftime("%d/%m/%Y")
TIME = today.strftime("%H:%M:%S")

param = {
    "workout": {
        "date": DATE,
        "time": TIME,
        "exercise": EXERCISE,
        "duration": DURATION,
        "calories": CALORIES
    }
}

response2 = requests.post(url=shetty_endpoint, json=param, headers=shetty_header)
print(response2.text)
