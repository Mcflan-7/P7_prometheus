from ..wikimedia import WikipediaApi


class TestWikipedia():
    
    def test_if_title_is_return_from_api(self):
        wiki = WikipediaApi()
        title = wiki.get_title()
        assert title == "Deaflympics d'été de 1924"



FAKE_API_RESULT= {} # Remplacer par la structure de donnée désirée

class MockRequestsGet:
    def __init__(self, url, params=None):
        pass
    def json(self):
        return FAKE_API_RESULT