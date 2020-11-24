"""Config for the api and web server."""
import os

############## API CONFIG ##############

API_KEY = os.environ.get("API_KEY")
API_URL = f"https://maps.googleapis.com/maps/api/geocode/json?&key={API_KEY}"
