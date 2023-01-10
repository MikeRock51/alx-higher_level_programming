#!/usr/bin/python3
"""A module that writes to a file"""


def write_file(filename="", text=""):
    """
    Writes a string to a file

    Args:
        filename: A string containing the path to the file
        text: A string containing the string to write

    Return: The number of characters written
    """
    with open(filename, 'x+', encoding="UTF-8") as f:
        wr = f.write(text)
    return (wr)
