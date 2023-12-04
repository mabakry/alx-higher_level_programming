#!/usr/bin/python3
"""  class module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """ Instantiation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
