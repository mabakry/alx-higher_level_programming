#!/usr/bin/python3
""" class module"""


class Rectangle:
    """ defines a Rectangle"""
    def __init__(self, width=0, height=0):
        """ initiate witdh and height"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Private instance attribute: width"""
        return self.__width

    @property
    def width(self, value):
        """ setter to width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Private instance attribute: height"""
        return self.__height

    @property
    def height(self, value):
        """ setter to height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
