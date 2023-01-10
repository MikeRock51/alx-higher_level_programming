#!/usr/bin/python3
"""A module containing a class that inherits from BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square subclass to Rectangle"""
    def __init__(self, size):
        """Initializes a Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of a Square"""
        return (self.__size ** 2)
