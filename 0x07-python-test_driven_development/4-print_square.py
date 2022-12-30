#!/usr/bin/python3
"""Module that prints a square with the character #"""

def print_square(size):
    """Function that prints a squre by representing it with #
    
    Args:
        size: The length of the square

    Raises:
        TypeError: If size is not an integer 
        TypeError: If size is a float and is less than 0
        ValueError: If size is less than 0
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

# print_square(4)