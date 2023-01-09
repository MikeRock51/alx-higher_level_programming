#!/usr/bin/python3
"""A module containing a class called BaseGeometry"""


class BaseGeometry(object):
    """A class with one method that raises an exception"""

    def area(self):
        raise Exception("area() is not implemented")
