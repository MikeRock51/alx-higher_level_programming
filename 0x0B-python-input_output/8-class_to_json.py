#!/usr/bin/python3
"""Module that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object"""
import json


def class_to_json(obj):
    """
    Returns dictionary description of an object

    Args:
        my_obj: Object to describe
    """
    return (obj.__dict__)
