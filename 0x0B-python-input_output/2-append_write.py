#!/usr/bin/python3
"""A module that appends to a file"""


def append_write(filename="", text=""):
    """
    Appends a string to a file

    Args:
        filename: A string containing the path to the file
        text: A string containing the string to append

    Return: The number of characters written
    """
    with open(filename, 'a+', encoding="UTF-8") as f:
        wr = f.write(text)
    return (wr)
