"""  Module using the Geocoding and Wikimedia API to generate a story for a given location """

from .cleaner import DataCleaner
from .geocoding import GeocodingApi
from .parser import ParserData
from .wikimedia import WikipediaApi


class BotPy:
    """ Class that create instances for the front end """

    def __init__(self, question):
        self.parser = ParserData()
        self.cleaner = DataCleaner()
        self.question = question

    def give_answer_for_client(self):
        """Given the data received by the method
        it will give a short story of the location with a link to
        read the full story.

        Returns:
            dict: Return an anwser with uselful data
        """
        parsed_data = self.parser.isolated_data(self.question)
        location = self.cleaner.normalize_data(parsed_data)
        self.geocoding = GeocodingApi(location)
        lattitude, longitude = self.geocoding.get_location_information()
        wiki = WikipediaApi(lattitude, longitude)

        story_title = wiki.get_title()
        story_extract = wiki.get_extract()
        story_url = wiki.get_url()

        data = {
            "title": story_title,
            "article": story_extract,
            "url": story_url,
            "question": location,
            "lat": lattitude,
            "lng": longitude
        }

        return data