import requests
import pandas as pd
import matplotlib.pyplot as plt

# Constants
API_KEY = "6af5c790409e4b909ff84ec99ef1e401"
CITIES = ["Chennai", "Mumbai", "Delhi", "Kolkata", "Bengaluru"]
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to get weather data for a city
def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            "City": city,
            "Temperature (°C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Description": data["weather"][0]["description"]
        }
    else:
        print(f"Error for {city}: {response.json().get('message', 'No data')}")
        return None

# Fetch weather for all cities
weather_data = [get_weather(city) for city in CITIES]
weather_data = [data for data in weather_data if data is not None]

# Create and display DataFrame
df = pd.DataFrame(weather_data)
print(df)

# Plot temperature comparison
plt.figure(figsize=(10, 5))
plt.bar(df["City"], df["Temperature (°C)"], color="lightcoral")
plt.title("Temperature Comparison")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()
