from ..parser import ParserData

parser = ParserData()
print()


class TestDataParser:
    """ Test if input data is isolated"""

    def test_if_data_is_isolated(self):
        """Test if data is isolated"""
        input_example = "Bonjour Gaëtan, où se trouve Paris ?"
        assert parser.isolated_data("Bonjour  , où se trouve Paris ?") == ("Paris")
