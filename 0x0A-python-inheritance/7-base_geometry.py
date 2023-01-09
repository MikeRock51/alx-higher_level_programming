#!/usr/bin/python3
"""A module containing a class called BaseGeometry"""


class BaseGeometry(object):
    """A class with some methods that raises an exception
    and validates integer respectively"""

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
