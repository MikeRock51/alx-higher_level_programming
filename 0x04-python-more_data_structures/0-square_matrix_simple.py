#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_sqr = [list(map(lambda x: x ** 2, lst)) for lst in matrix]
    return (matrix_sqr)
