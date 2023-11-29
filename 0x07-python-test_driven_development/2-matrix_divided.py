#!/usr/bin/python3
def matrix_divided(matrix, div):
    """  divides all elements of a matrix."""

    m = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("{}".format(m))

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("{}".format(m))

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for j in row:
            if type(j) not in (int, float):
                raise TypeError("{}".format(m))

    return [[round(j / div, 2) for j in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
