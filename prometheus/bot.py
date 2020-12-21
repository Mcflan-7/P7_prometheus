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
    def __init__(self):
        self.parser = ParserData()
        self.cleaner = DataCleaner()
        self.wiki = WikipediaApi()

    def get_question_from_client(self, question):
        parsed_data = self.parser.isolated_data(question)
        location = self.cleaner.normalize_data(parsed_data)
        return location

    def give_answer_for_client(self, location):
        self.geocoding = GeocodingApi(location)
        lattitude, longitude = self.geocoding.get_location_information()
        answer = self.wiki.get_data(lattitude, longitude)
        return answer


if __name__ == "__main__":
    bot = BotPy()
    data = bot.get_question_from_client("Où se trouVe paris?")
    print(bot.give_answer_for_client(data))
