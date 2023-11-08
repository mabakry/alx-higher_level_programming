#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = map(lambda row: map(lambda x: x * x, row), matrix)
    new = list(list(row) for row in new)
    return (new)
