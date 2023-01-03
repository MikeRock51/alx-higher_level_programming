#!/usr/bin/python3
"""A modiule containing a locked class"""


class LockedClass:
    """Only creates an instance if the attribute = first_name"""

    __slots__ = ["first_name"]
