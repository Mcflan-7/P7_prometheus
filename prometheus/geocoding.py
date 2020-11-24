""" Handle the geocoding logic with Google Maps Geocoding API """
import requests

from .constant import API_URL_GEOCODING

request_location = "Paris"
payload = {"language": "fr", "address": request_location}

r = requests.get(API_URL_GEOCODING, params=payload).json()

city_name = r["results"][0]["address_components"][0]["long_name"]
county = r["results"][0]["address_components"][2]["long_name"]
lattitude = r["results"][0]["geometry"]["location"]["lat"]
longitude = r["results"][0]["geometry"]["location"]["lng"]
