""" Test module for geocoding using Pytest """
import requests

from ..geocoding import GeocodingApi

# Mocking JSON response when request is sent to the Geocoding API
MOCK_GEOCODING_SUCCESS = {'results': [{'address_components': [{'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']}, {'long_name': 'Département de Paris', 'short_name': 'Département de Paris', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Île-de-France', 'short_name': 'IDF', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}], 'formatted_address': 'Paris, France', 'geometry': {'bounds': {'northeast': {'lat': 48.9021449, 'lng': 2.4699208}, 'southwest': {'lat': 48.815573, 'lng': 2.224199}}, 'location': {'lat': 48.856614, 'lng': 2.3522219}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 48.9021449, 'lng': 2.4699208}, 'southwest': {'lat': 48.815573, 'lng': 2.224199}}}, 'place_id': 'ChIJD7fiBh9u5kcRYJSMaMOCCwQ', 'types': ['locality', 'political']}], 'status': 'OK'}
      

print(MOCK_GEOCODING_SUCCESS)

class MockResponse200:
    """Mock 200 response for requests."""

    status_code = 200

    def json(self):
        """Mocking json response from API

        Returns:
            Dict: Data received from api if succesful
        """
        return MOCK_GEOCODING_SUCCESS


def mock_requests_get_success(url, params=None):
    """Mock get method from requests if success"""
    return MockResponse200()


class TestGeocoding:
    """Test geocoding class with monkeypatch"""

    geocoding = GeocodingApi("Paris")

    def test_geocoding_get_lat_and_long_return_(self, monkeypatch):
        """ If requests is successfull, test should return the long and lat of a location """

        monkeypatch.setattr("requests.get", mock_requests_get_success)
        # lattitude and longitude are assigned
        lattitude, longitude = self.geocoding.get_location_information()
        # and unpacked .. 
        assert MOCK_GEOCODING_SUCCESS["results"][0]["geometry"]["location"]["lat"] == lattitude
        assert MOCK_GEOCODING_SUCCESS["results"][0]["geometry"]["location"]["lng"] == longitude

