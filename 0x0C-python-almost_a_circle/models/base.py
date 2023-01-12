#!/usr/bin/python3
"""This module contains the base class for this project"""


class Base:
    """The base class for our project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base object contructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
