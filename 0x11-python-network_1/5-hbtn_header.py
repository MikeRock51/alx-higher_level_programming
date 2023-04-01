#!/usr/bin/python3
"""
Sends a request to the given URL and displays the value of the variable
X-Request-Id in the response header
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    res = requests.get(argv[1])
    for key, value in res.headers.items():
        if key == 'X-Request-Id':
            print(value)
            break
