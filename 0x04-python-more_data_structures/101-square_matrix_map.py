#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return(list(map(lambda outer: list(map(lambda inner: inner * inner, outer)), matrix)))
