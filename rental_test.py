import unittest
from rental import Rental, PriceCode
from movie import *
from datetime import datetime


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Rang Zong", str(datetime.now().year), ['Horror'])
        self.regular_movie = Movie("Frozen", "2002", ["Documentary"])
        self.childrens_movie = Movie("The Irishman", "2017", ["Children"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Rang Zong", str(datetime.now().year), ['Horror'])
        self.assertEqual("Rang Zong", m.get_title())

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)
        rental = Rental(self.regular_movie, 2)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 100)
        self.assertEqual(rental.get_price(), 149.0)
        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 10)
        self.assertEqual(rental.get_price(), 12.0)

    def test_rental_points(self):
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_rental_point(), 5)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_rental_point(), 1)
        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.get_rental_point(), 1)
