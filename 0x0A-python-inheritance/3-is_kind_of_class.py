#!/usr/bin/python3
"""a module function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False."""


def is_kind_of_class(obj, a_class):
    """"Return True of false respectively"""

    if isinstance(obj, a_class) and issubclass(type(obj), a_class):
        return True
    return False
