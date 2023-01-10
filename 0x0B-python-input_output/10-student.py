#!/usr/bin/python3
"""A module containing a student class"""


class Student:
    """An object representation of a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary description of an object"""

        if isinstance(attrs, list) and\
                all(isinstance(item, str) for item in attrs):
            return ({key: getattr(self, key)
                    for key in attrs if hasattr(self, key)})
        return (self.__dict__)
