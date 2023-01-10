#!/usr/bin/python3
"""A module containing a student class"""


class Student:
    """An object representation of a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary description of an object"""
        return (self.__dict__)
