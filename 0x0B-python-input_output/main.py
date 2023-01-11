#!/usr/bin/python3
<<<<<<< HEAD
"""
12-main
"""
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
    
=======
append_after = __import__('100-append_after').append_after

append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
>>>>>>> 66bc6ca31e56ec9ec19c3c4aa03bb1416a3be32f
