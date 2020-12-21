import requests

from ..wikimedia import WikipediaApi

MOCK_WIKIPEDIA_SUCCESS = {
    "batchcomplete": "",
    "query": {
        "geosearch": [
            {
                "pageid": 6422233,
                "ns": 0,
                "title": "Jeux olympiques d'étédzdzdz de 2024",
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


class TestWikipedia:
    """Test wikipedia class with monkeypatch"""

    wiki = WikipediaApi()

    def test_wikimedia_get_info_return_is_successfull(self, monkeypatch):
        """ If requests is successfull, test should return dict """

        monkeypatch.setattr("requests.get", mock_requests_get_success)
        results = self.wiki.get_data(0, 0)
        assert MOCK_WIKIPEDIA_SUCCESS == results

    def test_wikimedia_return_title_from_api(self, monkeypatch):
        """ If requests is successfull, Should return title from dict """
        monkeypatch.setattr("requests.get", mock_requests_get_success)
        response = self.wiki.get_data(0, 0)
        results = self.wiki.get_title(response)
        assert MOCK_WIKIPEDIA_SUCCESS["query"]["geosearch"][0]["title"] == results
