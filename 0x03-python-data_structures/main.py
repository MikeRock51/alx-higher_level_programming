#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
n = []
max_value = max_integer(my_list)
max_v = max_integer(n)
print("Max: {}".format(max_value))
print("Max_V: {}".format(max_v))


