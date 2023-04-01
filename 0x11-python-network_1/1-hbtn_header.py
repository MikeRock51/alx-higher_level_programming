#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""


if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv

    with urlopen(argv[1]) as response:
        page = response.read()

    for variable in response.getheaders():
        if variable[0] == 'X-Request-Id':
            print(variable[1])
            break
