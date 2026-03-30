import requests

API_KEY = "3da3ddae0ec60baa5dc38fab69cee6c9"

def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    try:
        data = requests.get(url).json()
        
        if "wind" not in data:
            print(f"OpenWeather API Error for {lat}, {lon}: {data}")
            return 10.0, 1010.0, 5000.0 # Default fallback safe values

        wind = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        visibility = data["visibility"]
        
        return wind, pressure, visibility
    except Exception as e:
        print(f"Weather Exception: {e}")
        return 10.0, 1010.0, 5000.0
