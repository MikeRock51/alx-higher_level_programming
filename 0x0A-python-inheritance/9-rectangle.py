#!/usr/bin/python3
"""A module containing a class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle subclass to BaseGeometry"""

    def __init__(self, width, height):
        """Initializes the Rectangle class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of a Rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Return Rectangle description"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
