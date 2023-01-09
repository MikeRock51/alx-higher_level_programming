#!/usr/bin/python3
"""A module that demonstrates inheritance"""


class MyList(list):
    """A class that inherits from list object"""

    def __init__(self, lst=[]):
        self.lst = lst

    def print_sorted(self):
        """Prints a sorted list in ascending order"""

        print(sorted(self))
