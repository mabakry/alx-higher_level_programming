#!/usr/bin/python3
""" Module to check if the object is exactly
an instance of the specified class"""


def is_same_class(obj, a_class):
    """ returns True if he object is exactly
    an instance of the specified class otherwise False."""

    return type(obj) is a_class
