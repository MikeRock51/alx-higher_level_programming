#!/usr/bin/python3
import json
"""Module that returns the JSON representation of an object"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object

    Args:
        obj: Object to convert
    """
    return (json.dumps(my_obj))
