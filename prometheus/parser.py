""" Parse the sentence and keep valuable data """
import json

# je pose une question : "ou se trouve Paris ?" /// je dois récupérer que Paris

with open("prometheus/stopwords.json", "r") as f:
    stopword_fr = json.loads(f.read())


class ParserData:
    """ Parse data and isolate works"""

    def __init__(self):
        self.input_example = "Bonjour Gaëtan, où se trouve Paris ?"
        self.stopword_fr = stopword_fr

    def isolated_data(self, input_data):
        """ isolated keyword"""
        querywords = input_data.split()
        resultwords = [
            word for word in querywords if word.lower() not in self.stopword_fr
        ]  # list comprehension, word for word dans queryworld (liste de query)
        result = " ".join(resultwords)
        return result


if __name__ == "__main__":
    parser = ParserData()

    query = "Bonjour  , où se trouve Paris ?"  # input
    # stopworlds
    print(parser.isolated_data(query))
