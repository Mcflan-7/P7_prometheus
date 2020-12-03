from ..cleaner import DataCleaner
from ..parser import ParserData

parser = ParserData()
cleaner = DataCleaner()


class TestDataParser:
    """ Test if input data is isolated"""

    def test_if_data_is_isolated(self):
        """Test if data is isolated"""
        question_1 = "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense,\
             pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"

        question_2 = "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais\
             m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie."
        assert parser.isolated_data(cleaner.normalize_data(question_1)) == (
            "musee d'art d'histoire fribourg"
        )
        assert parser.isolated_data(cleaner.normalize_data(question_2)) == (
            "tour eiffel"
        )

    def test_if_data_is_empty_or_not(self):
        """Test if given data is empty or not"""
