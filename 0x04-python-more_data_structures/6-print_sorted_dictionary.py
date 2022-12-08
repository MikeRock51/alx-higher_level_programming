#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_list = sorted(list(a_dictionary.items()))
    sort_dict = dict(sort_list)

    for key, value in sort_dict.items():
        print('{}: {}'.format(key, value))
