import requests
import os
from dotenv import load_dotenv

def configure():
    load_dotenv()

def main():
    configure()

    city = "London"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('api_key')}"
    print(url)

    # Send a request to the API and retrieve the response
    response = requests.get(url)
    print(response.json())

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        temperature_C = data["main"]["temp"] - 273.15
        description = data["weather"][0]["description"]
        
        print(f"The current weather in {city} is {temperature_C:.2f}°C with {description}.")
    else:
        print("Failed to retrieve weather information.")

if __name__ == "__main__":
    main()