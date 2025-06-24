import requests

# ✅ Your API key (correct format)
API_KEY = "6af5c790409e4b909ff84ec99ef1e401"

# ✅ City to get weather info
city = "Chennai"

# ✅ Correct API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# ✅ Send request
response = requests.get(url)
data = response.json()

# ✅ Check if response is successful
if response.status_code == 200:
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    
    print(f"City: {city}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description}")
else:
    print("Error:", data.get("message", "Unable to fetch weather data"))
import requests
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = "6af5c790409e4b909ff84ec99ef1e401"
cities = ['Chennai', 'Mumbai', 'Delhi', 'Kolkata', 'Bengaluru']

weather_data = []

for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        weather_data.append({
            "City": city,
            "Temperature (°C)": data['main']['temp'],
            "Humidity (%)": data['main']['humidity'],
            "Description": data['weather'][0]['description']
        })
    else:
        print(f"Error for {city}: {data.get('message')}")

# Create DataFrame
df = pd.DataFrame(weather_data)
print(df)

# Plot bar chart
plt.figure(figsize=(10, 5))
plt.bar(df['City'], df['Temperature (°C)'], color='lightcoral')
plt.title('Temperature Comparison')
plt.xlabel('City')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()



