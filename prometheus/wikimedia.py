""" Handle the geocoding logic with Google Maps Geocoding API """

import requests

from .constant import API_URL_WIKIPEDIA


class WikipediaApi:
    """Request data from the wikipedia api"""

    def __init__(self, latitude, longitude):
        """Intialise the wikipedia instance
        Args:
            latitude (float): Latitude for the location
            longitude (float): Longitude for the location
        """
        self.wikipedia_url = API_URL_WIKIPEDIA
        self.latitude = latitude
        self.longitude = longitude
        self.params = {
            "format": "json", 
            "action": "query",  
            "prop": "extracts|info",
            "inprop": "url", 
            "exchars": 700, 
            "explaintext": True,
            "generator": "geosearch",
            "ggscoord": f"{self.latitude}|{self.longitude}"
        }
        self.response = requests.get(self.wikipedia_url, params=self.params).json()["query"]["pages"]
        self.data_list = list(self.response.values())

    def get_title(self):
        """Get the 1st title from wikipedia API

        Returns:
            str: Return the 1st title from an article
        """

        title = self.data_list[0]["title"]

        return title

    def get_extract(self):
        """Get the 1st extract from wikipedia API

        Returns:
            str: Return the 1st extract from an article
        """
        extract = self.data_list[0]["extract"]
        return extract

    def get_url(self):
        """Get the 1st url from wikipedia API

        Returns:
            str: Return the 1st url from an article
        """
        url = self.data_list[0]["fullurl"]

        return url
