#!/usr/bin/python3
"""
Sends a request to the given URL and displays the value of the variable
X-Request-Id in the response header
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    res = requests.get(argv[1])
    if hasattr(res, 'X-Request-Id'):
        print(res.headers["X-Request-Id"])
