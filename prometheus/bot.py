"""  Module using the Geocoding and Wikimedia API to generate a story for a given location """

from .cleaner import DataCleaner
from .geocoding import GeocodingApi
from .parser import ParserData
from .wikimedia import WikipediaApi

""" geocoding = GeocodingApi("Ou se trouve Marseille")
parser = ParserData()
data = parser.isolated_data("coucou grandpy ou se trouve paris?")
cleaner = DataCleaner()
print(cleaner.normalize_data(data))


print(geocoding)
lattitude, longitude = geocoding.get_location_information()

wiki = WikipediaApi()
response = wiki.get_data(lattitude, longitude)
print(wiki.get_title(response)) """


class BotPy:
    """ Class """

    def __init__(self, question):
        self.parser = ParserData()
        self.cleaner = DataCleaner()
        self.question = question

    def get_question_from_client(self):
        """Received question from the client and return the needed data.

        Args:
            question (str): Question from the client Ex: ("Where is Paris")

        Returns:
            str: Return location from the question once it is parsed and normalized.
        """
        parsed_data = self.parser.isolated_data(self.question)
        location = self.cleaner.normalize_data(parsed_data)
        return location

    def give_answer_for_client(self, location):
        """Given the data received by the method
        it will give a short story of the location with a link to
        read the full story.

        Args:
            location (str): City or location

        Returns:
            str: Return an anwser with a story and a link
        """
        self.geocoding = GeocodingApi(location)
        lattitude, longitude = self.geocoding.get_location_information()
        wiki = WikipediaApi(lattitude, longitude)
        story_title = wiki.get_title()
        story_extract = wiki.get_extract()
        story_url = wiki.get_url()

        return story_title, story_extract, story_url


if __name__ == "__main__":
    bot = BotPy("ou se trouve Paris?")
    location = bot.get_question_from_client()
    print(bot.give_answer_for_client(location))

