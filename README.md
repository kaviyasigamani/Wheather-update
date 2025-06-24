# 🌦️ Weather Data Visualization using OpenWeatherMap API

This project fetches real-time weather data for multiple Indian cities using the **OpenWeatherMap API**, displays the data in tabular form using **Pandas**, and visualizes the temperature using **Matplotlib**.

---

## 📌 Features

- Fetches live weather data (temperature, humidity, and condition)
- Supports multiple cities
- Displays weather data in a table
- Visualizes temperature using a bar chart

---

## 🛠️ Tools & Libraries Used

- `requests` – For sending HTTP requests to the API
- `pandas` – For handling and displaying data in tabular form
- `matplotlib` – For creating data visualizations

---

## 🚀 How It Works

### 1. API Setup

The project uses the **OpenWeatherMap API** to get live weather data for selected cities:

- Chennai
- Mumbai
- Delhi
- Kolkata
- Bengaluru

You must have an API key from [OpenWeatherMap](https://openweathermap.org/api) to access their data.

```python
API_KEY = "your_api_key_here"
````

---

### 2. Fetch Weather Data

For each city in the list, the script sends a request to the API:

```python
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
```

If the request is successful (`status_code == 200`), the script extracts:

* Temperature in Celsius (`temp`)
* Humidity percentage (`humidity`)
* Weather condition (`description`)

---

### 3. Create Data Table

All data is stored in a list of dictionaries, then converted to a Pandas DataFrame:

```python
df = pd.DataFrame(weather_data)
print(df)
```

This provides a neat, tabular format for weather data across cities.

---

### 4. Visualize the Data

A bar chart is created to compare temperatures across cities:

```python
plt.bar(df['City'], df['Temperature (°C)'], color='lightcoral')
plt.title('Temperature Comparison')
plt.xlabel('City')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()
```

This chart gives a visual comparison of the current temperatures in the selected cities.

---

## 📷 Sample Output

| City      | Temperature (°C) | Humidity (%) | Description     |
| --------- | ---------------- | ------------ | --------------- |
| Chennai   | 32               | 65           | clear sky       |
| Mumbai    | 30               | 70           | haze            |
| Delhi     | 35               | 40           | broken clouds   |
| Kolkata   | 31               | 68           | light rain      |
| Bengaluru | 28               | 60           | overcast clouds |

---

## 📦 Installation & Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/weather-visualization.git
cd weather-visualization
```

### 2. Install Required Libraries

```bash
pip install requests pandas matplotlib
```

### 3. Replace the API Key

Open the Python file and paste your OpenWeatherMap API key here:

```python
API_KEY = "your_api_key_here"
```

### 4. Run the Script

```bash
python weather.py
```

You will see both a table of weather data and a bar chart showing temperatures.

---

## 🧠 Learning Outcomes

* How to interact with public APIs in Python
* How to parse JSON data
* How to store and display data using Pandas
* How to visualize data using Matplotlib

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) – feel free to use, share, and modify it!

---

## 🙌 Acknowledgements

* [OpenWeatherMap API](https://openweathermap.org/)
* Python, Pandas, Matplotlib libraries

---

## ✍️ Author

**Your Name** – [Your GitHub Profile](https://github.com/your-username)
```
