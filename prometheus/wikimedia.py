""" Handle the geocoding logic with Google Maps Geocoding API """

import requests

from .constant import API_URL_WIKIPEDIA


class WikipediaApi:
    """Request data from the wikipedia api"""

    def __init__(self):
        self.payload = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
            "exchars": 400,
            "generator": "geosearch",
            "ggscoord": f"{48.856611}|{2.3522219}",  # dummies datas PARIS
        }
        self.r = requests.get(API_URL_WIKIPEDIA, params=self.payload).json()

    def get_title(self):
        """Get the title from API wikipedia information

        Returns:
            str: Title of the request
        """
        return self.r["query"]["pages"]["7738248"]["title"]

    def get_extract(self):
        """Get the extract from API wikipedia information

        Returns:
            str: Extract of the request
        """
        return self.r["query"]["pages"]["7738248"]["extract"]


if __name__ == "__main__":
    wiki = WikipediaApi()
    print(wiki.get_title())
    print(wiki.get_extract())
