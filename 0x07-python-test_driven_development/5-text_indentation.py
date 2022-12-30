#!/usr/bin/python3
"""A module that prints a text with 2 new lines 
after each of these characters: ., ? and :"""

def text_indentation(text):
    """Prints text with 2 new lines after every '.', '?' and ':'
    
    Args:
        text: The text to print
    
    Raises:
        TypeError: If text is not a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    t = 0
    for c in text:
        if c == ' ' and t == 0:
            continue
        print(c, end="")
        t = 1
        if c == "." or c == "?" or c == ":":
            print()
            print()
            t = 0

# text_indentation("       Messi is the GOAT.    ")