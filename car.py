class Car:
    """ Represents a car in a car lot"""

    def __init__(self, make, model, year, cost, price):
        """ Initializes the car details """
        self._make = make
        self._model = model
        self._year = year
        self._cost = cost
        self._price = price

    def calc_profit(self):
        """ Returns the projected profit """
        return self._price - self._cost

    def get_details(self):
        """ Returns a formatted string with the car details"""
        details = "%d %s %s for sale for $%.2f" % (self._year, self._make, self._model, self._price)
        return details

    def reduce_price(self, reduction):
        """ Reduces the price value (self._price) by the reduction amount"""
        self._price = self._price - reduction
