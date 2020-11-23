from ..cleaner import DataCleaner


class TestDataCleaner:
    """ Test if received data is normalize and clean"""

    def test_if_data_is_normalized(self):
        """Test if data is checking cleaning requirements"""
        cleaner = DataCleaner()
        data_test = "Je suis un test"
        assert cleaner.normalize_data("je Suis un tEst") == data_test

    def test_if_data_has_not_special_character(self):
        """Test if data has not special characters"""
        cleaner = DataCleaner()
        assert cleaner.normalize_data("gâétân,.!?") == "Gaetan"
