#!/usr/bin/python3
"""Sends a POST request to the given URL with the given email as parameter"""


if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from sys import argv
    from urllib.parse import urlencode

    url = argv[1]
    email_Arg = argv[2]

    values = {'email': email_Arg}
    data = urlencode(values).encode('ascii')

    req = Request(url, data)
    with urlopen(req) as response:
        body = response.read()

    print(body)
