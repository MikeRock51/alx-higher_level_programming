#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda out: list(map(lambda inn: inn * inn, out)), matrix))
