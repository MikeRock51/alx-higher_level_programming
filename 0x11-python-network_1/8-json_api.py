#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) < 2:
        param = {"q": ""}
    else:
        param = {"q": argv[1]}

    res = requests.post('http://0.0.0.0:5000/search_user', data=param)

    try:
        json_res = res.json()
        if json_res == {}:
            print("No result")
        else:
            print(f"[{json_res['id']}] {json_res['name']}")
    except Exception:
        print("Not a valid JSON")
