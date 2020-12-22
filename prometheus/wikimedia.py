""" Handle the geocoding logic with Google Maps Geocoding API """

import requests

from .constant import API_URL_WIKIPEDIA


class WikipediaApi:
    """Request data from the wikipedia api"""

    def __init__(self, latitude, longitude):
        self.wikipedia_url = API_URL_WIKIPEDIA
        self.latitude = latitude
        self.longitude = longitude


    def get_title(self):
        """Get the 1st title from wikipedia API

        Args:
            response (dict): Response from the api in a dictionary

        Returns:
            str: Return the 1st title from an article
        """
        payload = {
            "format": "json",
            "action": "query",
            "list": "geosearch",
            "gsradius": 10000,
            "gscoord": f"{self.latitude}|{self.longitude}",
        }
        response = requests.get(self.wikipedia_url, params=payload).json()
        title = response["query"]["geosearch"][0]["title"]

        return title

    def get_extract(self):
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
            "ggscoord": f"{self.latitude}|{self.longitude}",  # Renvoyer du texte brut (éliminer les balises de markup)
        }
        extract = requests.get(self.wikipedia_url, params=params).json()["query"][
            "pages"
        ]["7785129"]["extract"]
        return extract

    def get_url(self):
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
            "ggscoord": f"{self.latitude}|{self.longitude}",  # Renvoyer du texte brut (éliminer les balises de markup)
        }
        url = requests.get(self.wikipedia_url, params=params).json()["query"]["pages"][
            "7785129"
        ]["fullurl"]

        return url



if __name__ == "__main__":
    wiki = WikipediaApi(48.856611, 2.3522219 )
    print(wiki.get_title())
    print(wiki.get_extract())