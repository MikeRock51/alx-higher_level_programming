#!/usr/bin/python3
""" A module that computes the addition of two numbers"""


def add_integer(a, b=98):
    """Function returns an integer, which is the sum of a and b
    args:
        a=> Num 1
        b=> Num 2

    Returns:
        The sum of a and b

    Raises:
        TypeError if a or b is neither a int or a float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
