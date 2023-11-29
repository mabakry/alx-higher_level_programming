#!/usr/bin/python3
def matrix_divided(matrix, div):
    """  divides all elements of a matrix."""

    new_matrix = [[]]
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        if i != 0 and len(i) != len(i - 1):
            raise TypeError("Each row of the matrix must have the same size")

        for j in i:
            if type(j) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            new_matrix.append("{:.2f}".format(j / div))

    return new_matrix
