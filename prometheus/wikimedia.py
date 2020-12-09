""" Handle the geocoding logic with Google Maps Geocoding API """

from pprint import pprint

import requests

from .constant import API_URL_WIKIPEDIA


class WikipediaApi:
    """Request data from the wikipedia api"""

    def __init__(self):
        self.wikipedia_url = API_URL_WIKIPEDIA

    def get_data(self, latitude, longitude):
        """Get data from wikipedia API for a given latitude et longitude

        Args:
            latitude (float): Latitude coords
            longitude (float): Longitude coords

        Returns:
            Dict: Data in a dict for the given latitude et longitude
        """
        payload = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
            "exchars": 400,
            "generator": "geosearch",
            "ggscoord": f"{latitude}|{longitude}",
        }
        response = requests.get(self.wikipedia_url, params=payload).json()
        return response


if __name__ == "__main__":
    wiki = WikipediaApi()
    print(wiki.get_data(48.856611, 2.3522219))
