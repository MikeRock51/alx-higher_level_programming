#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError as e:
        print("Exception: {:s}".format(str(e)))
        return False
