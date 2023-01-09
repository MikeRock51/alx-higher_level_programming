#!/usr/bin/python3
"""A module that demonstrates inheritance"""


class MyList(list):
    """A class that inherits from list object"""

    def print_sorted(self):
        """Prints a sorted list in ascending order"""

        print(sorted(self))
