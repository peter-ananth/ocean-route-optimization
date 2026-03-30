import requests

API_KEY = "b2af11c2-7413-11f0-b926-0242ac130006-b2af1262-7413-11f0-b926-0242ac130006"

def get_ocean(lat, lon):
    url = f"https://api.stormglass.io/v2/weather/point?lat={lat}&lng={lon}&params=waveHeight,currentSpeed"
    headers = {"Authorization": API_KEY}
    try:
        data = requests.get(url, headers=headers).json()
        
        if "hours" not in data or len(data["hours"]) == 0:
            print(f"StormGlass API Error for {lat}, {lon}: {data}")
            return 2.0, 1.0 # Default fallback safe values
            
        hour_data = data["hours"][0]
        
        # Fallback to 'sg' if 'noaa' is missing
        wave = hour_data.get("waveHeight", {}).get("noaa", hour_data.get("waveHeight", {}).get("sg", 2.0))
        current = hour_data.get("currentSpeed", {}).get("noaa", hour_data.get("currentSpeed", {}).get("sg", 1.0))

        return wave, current
    except Exception as e:
        print(f"Ocean Exception: {e}")
        return 2.0, 1.0
