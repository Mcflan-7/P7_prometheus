""" Clean the data received by the API in a human readable way"""
import unicodedata


class DataCleaner:
    def __init__(self):
        self.data = []

    def normalize_data(self, data):
        """Normalize the data"""

        cleaned_data = (
            unicodedata.normalize("NFD", data).encode("ascii", "ignore").decode("utf-8")
        )
        cleaned_data = str(cleaned_data).lower().capitalize()
        return cleaned_data


if __name__ == "__main__":
    cleaner = DataCleaner()
    clean = cleaner.normalize_data("eéééé")
    print(clean)
