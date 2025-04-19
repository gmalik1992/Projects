import os
from pprint import pprint

import requests
from dotenv import load_dotenv

load_dotenv()


def get_nearby_locations(location):
    """
    Fetch nearby locations for a given city.

    Args:
        location (str): The name of the city or place to search for nearby locations.

    Returns:
        list[dict]: A JSON response containing location data. If the request fails, it returns an error dictionary.
    """
    url = "https://ai-weather-by-meteosource.p.rapidapi.com/find_places"

    querystring = {"text": location}

    headers = {
        "x-rapidapi-key": os.getenv("API_KEY"),
        "x-rapidapi-host": os.getenv("API_HOST"),
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()


def get_location_geo_params(locations: list, name=None, place_id=None):
    """
    Extract geographical parameters (latitude, longitude, timezone) for a specific location.

    Args:
        locations (list): A list of location dictionaries returned by the `get_nearby_locations` function.
        name (str, optional): The name of the location to find. Defaults to None.
        place_id (str, optional): The unique identifier (place ID) of the location to find. Defaults to None.

    Returns:
        dict or None: A dictionary containing geographical parameters (lat, lon, timezone, language, units).
                      Returns None if no matching location is found.
    """
    for location in locations:
        location_dict = {}
        if (place_id and place_id.strip() == location.get("place_id")) or (
            name and name.strip() == location.get("name")
        ):
            location_dict["lat"] = location.get("lat")
            location_dict["lon"] = location.get("lon")
            break
    geo_params = {
        "timezone": location.get("timezone"),
        "language": "en",
        "units": "auto",
    }
    geo_params = {**geo_params, **location_dict}
    if not location_dict:
        return None
    return geo_params


def get_weather_report(geo_params):
    """
    Fetch the current weather based on geographical parameters.

    Args:
        geo_params (dict): A dictionary containing geographical parameters such as latitude, longitude, timezone, and units.

    Returns:
        dict: A JSON response containing the current weather data. If the request fails, it returns an error dictionary.
    """

    url = "https://ai-weather-by-meteosource.p.rapidapi.com/current"

    querystring = geo_params

    headers = {
        "x-rapidapi-key": os.getenv("API_KEY"),
        "x-rapidapi-host": os.getenv("API_HOST"),
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()


if __name__ == "__main__":
    loc_list = get_nearby_locations(location="New Delhi")
    pprint(loc_list[:2])
    geo_params = get_location_geo_params(loc_list, place_id="new-delhi")
    print("\n--------------Params------------")
    pprint(geo_params)
    print("\n--------------Results------------")
    pprint(get_weather_report(geo_params=geo_params))
    print()
