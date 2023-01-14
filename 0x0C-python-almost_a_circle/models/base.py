#!/usr/bin/python3
"""This module contains the base class for this project"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list-dictionary"""
        json_list = []
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '"[]"'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string respresentation of list_obj to a file"""

        list_dict = []
        with open('{}.json'.format(cls.__name__), 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('"[]"')
            else:
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                f.write(Base.to_json_string(list_dict))

    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return '"[]"'
        return json.loads(json_string)
