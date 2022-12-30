#!/usr/bin/python3
"""This module prints given full name"""

def say_my_name(first_name, last_name=""):
    """Prints First name, followed by last name
    
    Args:
        first_name: First name argument
        last_name: Last name argument

    Raises:
        TypeError: if either first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))

# say_my_name("Michael")