#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """Returns the peak from list_of_integers"""

    if not list_of_integers or list_of_integers == []:
        return None

    i = 1
    peak = []
    while i < len(list_of_integers):
        if list_of_integers[i] > list_of_integers[i -1] and list_of_integers[i] > list_of_integers[i +1]:
            peak.append(list_of_integers[i])
        i += 2

    if peak == []:
        return (max(list_of_integers))
    else:
        return (max(peak))
