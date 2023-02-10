import requests
import os

class WeatherData:
    def __init__(self):
        self.api_key = os.getenv('api_key')

    def fetch_lat_lon(self, city_name):
        '''
        Returns a tuple containing (latitude, longitude) co-ordinates for specified 'city_name'
        '''
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={os.getenv('api_key')}"
        
        response = requests.get(url)
        if response.status_code == 200:
            return (response.json()[0]["lat"], response.json()[0]["lon"])
        else:
            return None
    
    def fetch_history(self, lat, lon, start=None, end=None):
        '''
        Returns a dictionary of historical temperature data in the format {datetime:temperature}
        '''
        if start and end:
            url = f"https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&start={start}&end={end}&appid={os.getenv('api_key')}"
        else:
            url = f"https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&appid={os.getenv('api_key')}"
    
        response = requests.get(url)
        if response.status_code != 200:
            return None
        
        temp_history = {}
        for i in range(24):
            dt = response.json()["list"][i]["dt"]
            temp_C = round(response.json()["list"][i]["main"]["temp"] - 273.15, 2)

            temp_history[dt] = temp_C

        return temp_history