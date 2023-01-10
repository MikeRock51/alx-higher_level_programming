#!/usr/bin/python3
"""Module that writes an Object to a text file,
using a JSON representation:"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to text file in JSON format

    Args:
        my_obj: Object to write
        filename: File to write to
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f, ensure_ascii=False)
