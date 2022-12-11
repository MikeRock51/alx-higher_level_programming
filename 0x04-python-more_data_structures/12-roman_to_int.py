#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return (0)

    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_value = 0
    for note in reversed(roman_string):
        roman_value = values[note]
        if int_value < roman_value * 5:
            int_value += roman_value
        else:
            int_value -= roman_value
    return (int_value)
