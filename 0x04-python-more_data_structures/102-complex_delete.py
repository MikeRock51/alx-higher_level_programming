#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    d_list = []
    for key, val in a_dictionary.items():
        if val == value:
            d_list.append(key)

    for key in d_list:
        del a_dictionary[key]
    return (a_dictionary)
