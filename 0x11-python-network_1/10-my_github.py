#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the GitHub
API to display your id
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    username = argv[1]
    token = argv[2]
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"Bearer {token}"}

    res = requests.get(url, headers=headers)
    user_info = res.json()

    if "id" not in user_info.keys():
        print(None)
    else:
        print(user_info["id"])
