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