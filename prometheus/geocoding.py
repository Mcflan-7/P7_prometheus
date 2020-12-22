""" Handle the geocoding logic with Google Maps Geocoding API """
import requests

from .constant import API_URL_GEOCODING


class GeocodingApi:
    """Request data from the geocoding api"""

    def __init__(self, request_location):
        """Define the arguments for the geocoding API

        Args:
            request_location (str): Location to be searched
        """
        self.payload = {"language": "fr", "address": request_location}
        try:
            self.r = requests.get(API_URL_GEOCODING, params=self.payload).json()
        except requests.ConnectionError:
            print("Unable to get data from the API")

    def get_location_information(self):
        """Get the useful information for a given location

        Returns:
            str: Title of the request
        """
        lattitude = self.r["results"][0]["geometry"]["location"]["lat"]
        longitude = self.r["results"][0]["geometry"]["location"]["lng"]
        return lattitude, longitude
