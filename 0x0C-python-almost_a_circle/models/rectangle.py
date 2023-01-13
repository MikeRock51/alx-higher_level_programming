#!/usr/bin/python3
"""A module containing a Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """A class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter method"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Width setter method"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter method"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X getter method"""

        return self.__x

    @x.setter
    def x(self, value):
        """X setter method"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter method"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints a rectangle to standard output with # character"""
        i = 0
        while i < self.__height:
            if i == 0:
                print('\n' * self.__y, end='')
            print(' ' * self.__x, end='')
            print("#" * self.__width)
            i += 1

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format\
            (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Assigns argument to each attribute"""

        if args and len(args) > 0:
            index = 0
            for arg in args:
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.__width = arg
                elif index == 2:
                    self.__height = arg
                elif index == 3:
                    self.__x = arg
                elif index == 4:
                    self.__y = arg
                index += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
            