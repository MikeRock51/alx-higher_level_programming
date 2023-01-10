#!/usr/bin/python3
"""A module that adds new attribute to an object"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds new attribute to an object when possible

    Args:
        obj: Object to add to
        attr_name: Name of attribute to add
        attr_value: Value of the attribute

    Raises:
        TypeError: If object can't have new attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
