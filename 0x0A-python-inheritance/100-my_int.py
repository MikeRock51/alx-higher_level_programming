#!/usr/bin/python3
"""A module containing a rebel int class"""


class MyInt(int):
    """A rebel int class that inverts the default comparison operator"""

    def __eq__(self, value):
        """Inverts the == operator"""
        return (self.real != value)

    def __ne__(self, value):
        """Inverts the != operator"""
        return (self.real == value)
