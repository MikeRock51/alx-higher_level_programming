#!/usr/bin/python3
"""A module that verifies if a given object is
an instance of a specified object"""


def is_same_class(obj, a_class):
    """Returns True or False"""

    if isinstance(obj, a_class):
        return True
    return False
