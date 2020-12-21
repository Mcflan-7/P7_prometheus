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
            "format": "json",
            "action": "query",
            "list": "geosearch",
            "gsradius": 10000,
            "gscoord": f"{latitude}|{longitude}",
        }
        response = requests.get(self.wikipedia_url, params=payload).json()
        return response

    def get_title(self, response):
        """Get the 1st title from wikipedia API

        Args:
            response (dict): Response from the api in a dictionary

        Returns:
            str: Return the 1st title from an article
        """

        title = response["query"]["geosearch"][0]["title"]

        return title

    def get_extract(self, response):
        """Get the 1st extract from wikipedia API

        Args:
            response (dict): Response from the api in a dictionary

        Returns:
            str: Return the 1st extract from an article
        """
        params = {
            "format": "json",  # format de la réponse
            "action": "query",  # action à effectuer
            "prop": "extracts|info",  # Choix des propriétés pour les pages requises
            "inprop": "url",  # Fournit une URL complète, une URL de modification, et l’URL canonique de chaque page.
            "exchars": 1200,  # Nombre de caractères à retourner
            "explaintext": True,
            "generator": "geosearch",
            "exintro": True,
            "ggscoord": f"{48.856611}|{2.3522219}",  # Renvoyer du texte brut (éliminer les balises de markup)
        }
        extract = requests.get(self.wikipedia_url, params=params).json()["query"][
            "pages"
        ]["7785129"]["extract"]
        url = requests.get(self.wikipedia_url, params=params).json()["query"]["pages"][
            "7785129"
        ]["fullurl"]
        return extract, url


if __name__ == "__main__":
    wiki = WikipediaApi()
    response = wiki.get_data(48.856611, 9.3522219)
    print(wiki.get_title(response))
