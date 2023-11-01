#!/usr/bin/python3
def magic_calculation(a, b, c):
    if (a < b):
        return c
    elif (c > b):
        return (bin(a) + bin(b))
    else:
        return ((bin(a) * bin(b)) - bin(c))
