""" Parse the sentence and keep valuable data """
import json

with open("prometheus/data/stopwords.json", "r") as f:
    stopword_fr = json.loads(f.read())


class ParserData:
    """ Parse data from the user and keep useful information"""

    def __init__(self):
        self.stopword_fr = stopword_fr

    def isolated_data(self, input_data):
        """Isolate data from guest input
        and keep the valuable informations

        Args:
            input_data (str): Data to be parsed

        Returns:
            str: Return the word or sentence to lookup
        """
        querywords = input_data.split()
        resultwords = [
            word for word in querywords if word.lower() not in self.stopword_fr
        ]  # list comprehension, word for word dans queryworld (liste de query)
        result = " ".join(resultwords)
        return result
