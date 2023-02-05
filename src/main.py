import requests
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

city = "London"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('api_key')}"

# Send a request to the API and retrieve the response
response = requests.get(url)
print(response.json())

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    
    print(f"The current weather in {city} is {temperature}°C with {description}.")
else:
    print("Failed to retrieve weather information.")