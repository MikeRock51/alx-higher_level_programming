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

        if type(value) is not int:
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

        if type(value) is not int:
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

        if type(value) is not int:
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

        if type(value) is not int:
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
        """Overrides default __str__ method"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Assigns argument to each attribute"""

        attribute_keys = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for index in range(len(args)):
                setattr(self, attribute_keys[index], args[index])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of a Rectangle"""

        rect_dict = {'id': self.id, 'width': self.__width, 'height':
                     self.__height, 'x': self.__x, 'y': self.__y}
        return rect_dict
