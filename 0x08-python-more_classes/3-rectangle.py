#!/usr/bin/python3
"""A module containing a class representation of a rectange"""


class Rectangle:

    """A class representation of a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializer of a rectangle class

        Args:
            Width: The width of the rectangle
            Height: The height of the rectangle

        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is less than 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gets and return the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets and return the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Computes the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Prints rectangle with the # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        height = self.__height
        rect = ""
        while height > 0:
            rect += "#" * self.__width
            if height - 1 > 0:
                rect += '\n'
            height -= 1
        return (rect)
