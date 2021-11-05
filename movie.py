import csv


class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title: str, year: str, genre: list):
        # Initialize a new movie.
        self.__title = title
        self.__year = year
        self.__genre = genre

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def get_genre(self):
        return self.__genre

    def is_genre(self):
        if str in self.__genre:
            return True
        else:
            return False

    def __str__(self):
        return self.__title


class MovieCatalog:
    def __init__(self):
        self.catalog = []
        self.index = 0

    def add_catalog(self):
        with open("movies.csv", "r") as raw_data:
            rows = list(csv.reader(raw_data))
            for i in range(len(rows)):
                self.catalog.append(Movie(rows[i][1], rows[i][2], rows[i][3].split(sep='|')))

    def get_movie(self, title: str):
        for i in self.catalog:
            if i == title:
                return self.catalog[i]
            else:
                try:
                    self.add_catalog()
                except ValueError:
                    break
