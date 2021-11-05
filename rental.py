from datetime import datetime
from enum import Enum


class Rental:
    """
    A rental of a movie by customer.
	From Fowler's refactoring example.

	A realistic Rental would have fields for the dates
	that the movie was rented and returned, from which the
	rental period is calculated.
	But for simplicity of the example only a days_rented
    field is used.
    """

    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
		   a movie with known rental period (daysRented).
		"""
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = PriceCode.for_movie(movie)

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price(self):
        return self.price_code.price(self.days_rented)

    def get_rental_point(self):
        frequent_renter_points = 0
        frequent_renter_points += self.price_code.frequent_renter_point(self.days_rented)
        return frequent_renter_points


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    new_release = {"price": lambda days: 3.0 * days,
                   "frp": lambda days: days
                   }
    normal = {"price": lambda days: 2 + 1.5 * (days - 2),
              "frp": lambda days: 1
              }
    childrens = {"price": lambda days: 1.5 + 1.5 * (days - 3),
                 "frp": lambda days: 1
                 }

    def price(self, days: int) -> float:
        "Return the rental price for a given number of days"""
        pricing = self.value["price"]  # the enum member's price formula
        return pricing(days)

    def frequent_renter_point(self, days):
        frp = self.value["frp"]
        return frp(days)

    @classmethod
    def for_movie(cls, movie):
        price_code = cls.normal
        if movie.get_year() == str(datetime.now().year):
            price_code = cls.new_release
        elif "Children" in movie.get_genre():
            price_code = cls.childrens
        return price_code
