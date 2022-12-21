#!/usr/bin/python3
"""Validates the size of a square and computes it's area"""


class Square():
    """Defines a square and validates it's size"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with the given size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the size of a square"""
        return (self.__size)

    @property
    def position(self):
        """Returns the position of a square"""
        return (self.__position)

    @size.setter
    def size(self, value):
        """Sets the size of a square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Sets the position of a square"""
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                else:
                    raise TypeError("position must be a tuple"
                                    " of 2 positive integers")
            else:
                raise TypeError("position must be a tuple of"
                                " 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    """Computes the area of a square by acessing it's size"""
    def area(self):
        return (self.__size * self.__size)

    """Prints a square to stdout"""
    def my_print(self):
        if self.__size < 1:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.position[0], end='')
                print('#' * self.__size)
