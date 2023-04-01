#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order
to solve this challenge.

Requirements:
    The first argument will be the repository name
    The second argument will be the owner name
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    You don’t need to check arguments passed to the script
    (number or type)
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    res = requests.get(url)
    commits = res.json()

    for comms in commits[:10]:
        print(f"{comms['sha']}: {comms['commit']['author']['name']}")
