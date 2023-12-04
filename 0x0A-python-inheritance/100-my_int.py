#!/usr/bin/python3
""" rebel class module"""


class MyInt(int):
    """ rebel class"""
    def __eq__(self, value):
        """ inverts =="""
        return self.real != value

    def __ne__(self, value):
        """ inverts !="""
        return self.real == value
