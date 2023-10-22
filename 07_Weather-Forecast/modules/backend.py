import os
import requests

# Get API_KEY from an Env Variable
API_KEY = os.getenv("OPENWEATHER_API_KEY") # Get your key from https://openweathermap.org/api


def get_data(place, forecast_days=None):
    """
    Request data from the OpenWeather API based on the city/place parameter
    """
    # URL for the request
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    # Make request
    response = requests.get(url)
    # Get a dictionary with data
    data = response.json()
    # Filter data by the number of forecast days
    filtered_data = data["list"]
    num_values = 8 * forecast_days
    filtered_data = filtered_data[:num_values]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))