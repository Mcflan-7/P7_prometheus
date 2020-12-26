"""Config for the api and web server."""
import os

############## CONTSTANT APP  #################
SECRET_KEY = os.environ.get("SECRET_KEY")

############## CONSTANTS GEOCODING##############
API_KEY_GEOCODING = "AIzaSyCbn1GQVOld0hvqZI4GmN5vlHunZHWO_DY"
API_URL_GEOCODING = (
    f"https://maps.googleapis.com/maps/api/geocode/json?&key={API_KEY_GEOCODING}"
)

############## CONTSTANT WIKIPEDIA #################
API_URL_WIKIPEDIA = "https://fr.wikipedia.org/w/api.php"
