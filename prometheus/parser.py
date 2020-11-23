""" Parse the sentence and keep valuable data """
import json

from .cleaner import DataCleaner

# je pose une question : "ou se trouve Paris ?" /// je dois récupérer que Paris

with open("prometheus/stopwords.json", "r") as f:
    stopword_fr = json.loads(f.read())


class ParserData:
    """ Parse data and isolate works"""

    def __init__(self):
        self.input_example = "Bonjour Gaëtan, où se trouve Paris ?"
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


question_1 = "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"
question_2 = "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie."

cleaner = DataCleaner()

question_2 = cleaner.normalize_data(question_2)
question_1 = cleaner.normalize_data(question_1)

if __name__ == "__main__":
    parser = ParserData()

    print(parser.isolated_data(question_2))
