#!/usr/bin/python3
"""A module that divides all elements in a matrix"""


def matrix_divided(matrix, div):
    """Function divides every item of the matrix by div

    Args:
        matrix=> Matrix arguement
        div=> The number to divide by

    Raises:
        TypeError: if matrix is not a matrix, containing integers or float
        TypeError: if each row of the matrix is not the same length
        TypeError: if div is neither an integer nor a float
        ZeroDivisionError: If Div is 0

    Returns:
        A new matrix, containing the result of the division
    """
    if not isinstance(matrix, list) or not \
            all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    if any(type(item) not in [int, float] for row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(item / div, 2) for item in row] for row in matrix]
    return (new_matrix)
