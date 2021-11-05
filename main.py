# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer
from datetime import datetime


def make_movies():
    movies = [
        Movie("Weathering With You", "2020", ["Children"]),
        Movie("Jurassic World", '2015', ["Thriller"]),
        Movie("Frozen", "2002", ["Children"]),
        Movie("El Camino", str(datetime.now().year), ["Children"]),
        Movie("CitizenFour", str(datetime.now().year), ["Horror"])
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
