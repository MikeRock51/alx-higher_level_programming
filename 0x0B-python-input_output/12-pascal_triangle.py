#!/usr/bin/python3
"""A module containing a pascal triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s triangle of n"""

    if n <= 0:
        return (0)
