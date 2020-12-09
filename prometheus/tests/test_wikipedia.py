import requests

from ..wikimedia import WikipediaApi

MOCK_WIKIPEDIA_SUCCESS = {
    "batchcomplete": "",
    "query": {
        "geosearch": [
            {
                "pageid": 6422233,
                "ns": 0,
                "title": "Titre de test",
                "lat": 37.78785,
                "lon": -122.40065,
                "dist": 129.9,
                "primary": "",
            },
            {
                "pageid": 6422233,
                "ns": 0,
                "title": "Titre de test",
                "lat": 37.78785,
                "lon": -122.40065,
                "dist": 129.9,
                "primary": "",
            },
        ]
    },
}


class MockResponse200:
    """Mock 200 response for requests."""

    status_code = 200

    def json(self):
        """Mocking json response from API

        Returns:
            Dict: Data received from api if succesful
        """
        return MOCK_WIKIPEDIA_SUCCESS


def mock_requests_get_success(url, params=None):
    """Mock get method from requests if success"""
    return MockResponse200()


def test_wikimedia_get_info_return_is_successeful(monkeypatch):
    """ If requests is successeful, test should return dict """
    wiki = WikipediaApi()
    monkeypatch.setattr("requests.get", mock_requests_get_success)
    results = wiki.get_data(0, 0)
    assert MOCK_WIKIPEDIA_SUCCESS == results
