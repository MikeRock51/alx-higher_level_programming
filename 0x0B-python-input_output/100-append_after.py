#!/usr/bin/python3
"""Contains a function that inserts a line
of text to a file, after each
line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """Appends a given string immediately after
    the occurrence of a particular string"""

    new_file = ""

    with open(filename) as f:
        for line in f:
            new_file += line
            if search_string in line:
                new_file += new_string

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(new_file)
