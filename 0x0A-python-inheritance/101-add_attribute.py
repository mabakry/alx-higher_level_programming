#!/usr/bin/python3
""" adds a new attribute"""


def add_attribute(ob, name, value):
    """ adds a new attribute"""

    if not hasattr(ob, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(ob, name, value)
