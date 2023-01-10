#!/usr/bin/python3
"""A module that reads and print from a file"""


def read_file(filename=""):
    with open(filename) as f:
        myfile = f.read()
    print(myfile)
