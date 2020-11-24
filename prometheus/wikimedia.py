""" Handle the geocoding logic with Google Maps Geocoding API """
from pprint import pprint

import requests

from .constant import API_URL_WIKIPEDIA

payload = {
    "action": "query",
    "format": "json",
    "prop": "extracts",
    "exintro": True,
    "explaintext": True,
    "exchars": 400,
    "generator": "geosearch",
    "ggscoord": f"{48.856611}|{2.3522219}",  # dummies datas PARIS
}


r = requests.get(API_URL_WIKIPEDIA, params=payload).json()


pprint(r["query"]["pages"]["7738248"]["title"])  # return title
pprint(r["query"]["pages"]["7738248"]["extract"])  # return description
