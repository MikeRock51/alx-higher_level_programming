#!/usr/bin/python3
"""A module that reads and print from a file"""


def read_file(filename=""):
    """
    Reads and prints the contents of a file

    Args:
        filename: A string containing the path to the file
    """
    with open(filename, encoding="UTF-8") as f:
        myfile = f.read()
    print(myfile, end="")
