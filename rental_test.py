import unittest
from customer import Customer
from rental import Rental
from movie import *


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", PriceCode.NEW_RELEASE)
		self.regular_movie = Movie("CitizenFour", PriceCode.REGULAR)
		self.childrens_movie = Movie("Frozen", PriceCode.CHILDRENS)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", PriceCode.REGULAR)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.REGULAR, m.get_price_code())

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
		self.assertEqual(rental.get_point(), 5)
		rental = Rental(self.childrens_movie, 5)
		self.assertEqual(rental.get_point(), 1)
		rental = Rental(self.regular_movie, 5)
		self.assertEqual(rental.get_point(), 1)

