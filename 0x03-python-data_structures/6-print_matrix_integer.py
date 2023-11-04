#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = len(matrix)
    y = len(matrix[0])
    for i in range(0, x):
        for j in range(0, y):
            print("{:d}".format(matrix[i][j]), end="")
            if j != y - 1:
                print(" ", end="")
        print()
