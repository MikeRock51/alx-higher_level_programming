#!/usr/bin/python3
"""
A module to find a peak in a list of unsorted integers
And I think to myself, what a wonderful world
"""


def find_peak(list_of_integers):
    """
    Returns the peak from list_of_integers

    Params:
        list_integeri
    """

    if not list_of_integers or list_of_integers == []:
        return None

    i = 1
    peak = []
    while i < len(list_of_integers):
        if list_of_integers[i] > list_of_integers[i - 1] and\
        list_of_integers[i] > list_of_integers[i + 1]:
            peak.append(list_of_integers[i])
        i += 2

    if peak == []:
        return (max(list_of_integers))
    else:
        return (max(peak))
