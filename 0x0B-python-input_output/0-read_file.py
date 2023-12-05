#!/usr/bin/python3
""" Read file"""


def read_file(filename=""):
    """ Read File and Print it to STDOUT"""

    with open(filename) as f:
        print(f.read(), end="")
