"""Adapters 'adapt' one interface to allow a class to communicate with another
class that implements a different interface. Each public function in the adapter
is mapped to a function on the adapted interface"""

"""Age calculator class that uses dates in YYYY-MM-DD format instead
of the more common (and useful) Python datetime format"""
class AgeCalculator:
    def __init__(self, birthday):
        self.year, self.month , self.day = (
            int(x) for x in birthday.split("-")
        )

    def calculate_age(self, date):
        year, month, day = (int(x) for x in date.split("-"))
        age = year - self.year
        if (month, day) < (self.month, self.day):
            age -= 1
        return age


"""We want to be able to use the AgeCalculator class with datetime
dates (e.g. for interfacing with other objects in our program) so
we create an adapter class"""
import datetime

class DateAgeAdapter:
    """Convert datetime date into formatted string"""
    def _str_date(self, date):
        return date.strftime("%Y-%m-%d")

    def __init__(self, birthday):
        """Create AgeCalculator using composition"""
        birthday = self._str_date(birthday)
        self.calculator = AgeCalculator(birthday)

    def get_age(self, date):
        """Call method on adapted object"""
        date = self._str_date(date)
        return self.calculator.calculate_age(date)