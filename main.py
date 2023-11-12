import requests
from datetime import datetime
import os

# os.environ['API_ID'] = API_ID


API_KEY = os.environ['API_KEY']
API_ID = os.environ['API_ID']
END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = 'https://api.sheety.co/ef9118a3980eaab519ae6182ae3ac2f4/workOut/sheet1'

# EXERCISE = input('Enter what exercise you do ')

heders={
    "x-app-id":API_ID,
    "x-app-key":API_KEY,
    "Authorization": "Bearer sadghjsadgjgsja122"
}
query = {
    "query": 'pull up 100',
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}
response = requests.post(url=END_POINT,data=query,headers=heders)
print(response.text)
print(response.status_code)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)


    print(sheet_response.text)



