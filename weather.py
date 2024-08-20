from dotenv import load_dotenv
from pprint import pprint

import requests
import os

load_dotenv()


def get_current_weather(city="Pune"):

    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units=metric"

    # print(request_url)

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")

    city = input("\nPlease enter a city name : ")

    if not bool(city.strip()):
        city="Pune"

    weather_data = get_current_weather(city)
    print("\n")
    print(f"\nCurrent Weather for {weather_data['name']}")
    print(f"\nThe Temerature is {weather_data['main']['temp']}")
    print(f"\nFeels like {weather_data['weather'][0]['description']}")
