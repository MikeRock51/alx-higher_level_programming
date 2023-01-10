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
