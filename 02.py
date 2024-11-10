import requests


def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        print(f"Weather in {city_name.capitalize()}: {weather_description.capitalize()}")
        print(f"Temperature: {temperature_celsius:.2f}°C")
    else:
        print("Could not retrieve weather data. Please check the city name or try again later.")
        print(f"Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")


city_name = input("Enter the name of the locality: ")
api_key = "40fc6e5d95163bab077552331d00a48f"  # Use your actual API key here
get_weather(city_name, api_key)
