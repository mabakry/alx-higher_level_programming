#!/usr/bin/python3
""" class module"""


class Rectangle:
    """ defines a Rectangle"""
    def __init__(self, width=0, height=0):
        """ initiate a new Rectangle"""

        self.height = height
        self.width = width

    @property
    def width(self):
        """Get Rectangle Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Set Rectangle Width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Get Rectangle Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Set Rectangle Height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Calculate Rectangle Area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ Calculate Rectangle Perimeter"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """ Prints the Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ("")
        x = []
        for i in range(self.__height):
            for j in range(self.__width):
                x.append('#')
            if i != self.__height - 1:
                x.append("\n")
        return ("".join(x))

    def __repr__(self):
        """ Return string representation of ractangle"""
        x = "Rectangle(" + str(self.__width) + "," + str(self.__height) + ")"
        return (x)
