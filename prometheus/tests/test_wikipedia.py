""" Test module for wikipedia using Pytest """
import requests

from ..wikimedia import WikipediaApi

# Mocking JSON response when request is sent to the Wikipedia API
MOCK_WIKIPEDIA_SUCCESS = {
    "query": {
        "pages": {
            "5211": {
                "pageid": 5211,
                "ns": 0,
                "title": "Barcelone",
                "index": -1,
                "extract": "Barcelone [baʁsəlɔn] (en catalan : "
                "Barcelona [bərsəˈɫonə] ;",
                "fullurl": "https://fr.wikipedia.org/wiki/Barcelone",
            },
            "771897": {
                "pageid": 771897,
                "ns": 0,
                "title": "Quartier gothique",
                "index": 0,
                "fullurl": "https://fr.wikipedia.org/wiki/" "Quartier_gothique",
            },
            "1002545": {
                "pageid": 1002545,
                "ns": 0,
                "title": "Cités et Gouvernements locaux unis",
                "index": 1,
                "fullurl": "https://fr.wikipedia.org/wiki/"
                "Cit%C3%A9s_et_Gouvernements_locaux_unis",
            },
            "4082734": {
                "pageid": 4082734,
                "ns": 0,
                "title": "Palais de la généralité de Catalogne",
                "index": 2,
                "fullurl": "https://fr.wikipedia.org/wiki/Palais_"
                "de_la_g%C3%A9n%C3%A9ralit%C3%A9_de_Catalogne",
            },
        }
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

    def test_wikimedia_return_title_from_api(self, monkeypatch):
        """ If requests is successfull, Should return title from list """
        monkeypatch.setattr("requests.get", mock_requests_get_success)
        wiki = WikipediaApi(41.3825, 2.17694)
        data_list = list(MOCK_WIKIPEDIA_SUCCESS["query"]["pages"].values())
        results = wiki.get_title()
        assert data_list[0]["title"] == results

    def test_wikimedia_return_url_from_api(self, monkeypatch):
        """ If requests is successfull, Should return url from list """
        monkeypatch.setattr("requests.get", mock_requests_get_success)
        wiki = WikipediaApi(41.3825, 2.17694)
        data_list = list(MOCK_WIKIPEDIA_SUCCESS["query"]["pages"].values())
        results = wiki.get_url()
        assert data_list[0]["fullurl"] == results

    def test_wikimedia_return_extract_from_api(self, monkeypatch):
        """ If requests is successfull, Should return extract from list """
        monkeypatch.setattr("requests.get", mock_requests_get_success)
        wiki = WikipediaApi(41.3825, 2.17694)
        data_list = list(MOCK_WIKIPEDIA_SUCCESS["query"]["pages"].values())
        results = wiki.get_extract()
        assert data_list[0]["extract"] == results
