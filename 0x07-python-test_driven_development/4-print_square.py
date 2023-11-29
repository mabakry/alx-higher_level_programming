#!/usr/bin/python3
"""  prints a square"""


def print_square(size):
    """ prints a square with the character #"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
            j += 1
        print()
        i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
