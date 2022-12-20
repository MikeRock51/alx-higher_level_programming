#!/usr/bin/python3
"""Validates the size of a square and computes it's area"""


class Square():
    """Defines a square and validates it's size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """Computes the area of a square by acessing it's size"""
    def area(self):
        return (self.__size * self.__size)
