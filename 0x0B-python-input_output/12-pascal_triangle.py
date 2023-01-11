#!/usr/bin/python3
"""A module containing a pascal triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal’s triangle of n"""

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        triangle.append(row)
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    return triangle
