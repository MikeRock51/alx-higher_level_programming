#!/usr/bin/python3
"""A module containing a class representation of a rectange"""


class Rectangle:
    """A class representation of a Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def __str__(self) -> str:
        """Returns string representation of a rectangle with the # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        height = self.__height
        rect = ""
        while height > 0:
            rect += str(self.print_symbol) * self.__width
            if height - 1 > 0:
                rect += '\n'
            height -= 1
        return (rect)

    def __repr__(self):
        """Returns string representation of the triangle to
        recreate a new instance with eval"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest of 2 instances of a rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with equal width and height"""
        return (cls(size, size))
