#!/usr/bin/python3
"""class Student"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """  defines a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary"""
        return self.__dict__
