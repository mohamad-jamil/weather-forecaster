import os
from dotenv import load_dotenv

from WeatherData import WeatherData

def configure():
    load_dotenv()

def main():
    '''
    Main function for the weather forecasting application
    '''
    city_name = "London"
    
    configure()
    wd = WeatherData()
    lat, lon = wd.fetch_lat_lon(city_name)
    #print(f"{city_name} has latitude {lat} and longitude {lon}.")

    temp_history = wd.fetch_history(lat, lon)
    print(temp_history)

if __name__ == "__main__":
    main()