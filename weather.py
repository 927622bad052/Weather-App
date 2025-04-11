import requests

API_KEY = "your_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter city name: ")
url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    print(f"Temperature: {temp}°C")
    print(f"Weather: {desc}")
    print(f"Humidity: {humidity}%")
else:
    print("City not found.")
