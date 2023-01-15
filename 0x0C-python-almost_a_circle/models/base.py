#!/usr/bin/python3
"""This module contains the base class for this project"""

import json
import os
import csv


class Base:
    """The base class for our project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base object constructor"""
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
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_obj to a file"""

        list_dict = []
        with open('{}.json'.format(cls.__name__), 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                f.write(Base.to_json_string(list_dict))

    def from_json_string(json_string):
        """Returns a list of JSON string representation of json_string"""
        if json_string is None or len(json_string) == 0:
            return '[]'
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes already set"""
        dummy = cls(8, 6, 10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        instance_file = '{}.json'.format(cls.__name__)
        instance_list = []

        if not os.path.exists(instance_file):
            return '"[]"'

        with open(instance_file, 'r', encoding="utf-8") as f:
            json_str_list = f.read()

        json_dict_list = Base.from_json_string(json_str_list)

        for dic in json_dict_list:
            instance_list.append(cls.create(**dic))
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes an object list to a csv file"""

        file_name = '{}.csv'.format(cls.__name__)
        with open(file_name, 'w', newline='') as csvfile:
            if list_objs is None or len(list_objs) == 0:
                csvfile.write('[]')
            else:
                if file_name == "Rectangle.csv":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for dic in list_objs:
                    csv_writer.writerow(dic.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes an object list from a csv file"""

        file_name = '{}.csv'.format(cls.__name__)
        if file_name == "Rectangle.csv":
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        else:
            fieldnames = ['id', 'size', 'x', 'y']
        with open(file_name, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            csv_dict = [[key, int(value)] for key, value in csv_reader.items()]

        for obj in csv_dict:
            return cls.create(**obj)
