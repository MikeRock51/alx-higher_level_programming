#!/usr/bin/python3
"""A module that verifies if a given object is
an instance of a specified object"""


def is_same_class(obj, a_class):
    """Returns True or False"""

    return (type(obj) == a_class)
