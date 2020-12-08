"""Config for the api and web server."""
import os

############## CONTSTANT APP  #################
SECRET_KEY = os.environ.get("SECRET_KEY")

############## CONSTANTS GEOCODING##############
API_KEY_GEOCODING = os.environ.get("API_KEY")
API_URL_GEOCODING = (
    f"https://maps.googleapis.com/maps/api/geocode/json?&key={API_KEY_GEOCODING}"
)

############## CONTSTANT WIKIPEDIA #################
API_URL_WIKIPEDIA = "https://fr.wikipedia.org/w/api.php"
