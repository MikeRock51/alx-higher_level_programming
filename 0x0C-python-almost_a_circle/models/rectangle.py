#!/usr/bin/python3
"""A module containing a Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """A class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter method"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """Width setter method"""
        self.__width = width

    @property
    def height(self):
        """Height getter method"""
        return self.__height

    @height.setter
    def height(self, height):
        """Height setter method"""
        self.__height = height

    @property
    def x(self):
        """X getter method"""
        return self.__x

    @x.setter
    def x(self, x):
        """X setter method"""
        self.__x = x

    @property
    def y(self):
        """Y getter method"""
        return self.__y

    @y.setter
    def y(self, y):
        """Y setter method"""
        self.__y = y
