#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""


if __name__ == '__main__':
    import requests
    from sys import argv
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        req_dict = req.json()
        id = req_dict.get('id')
        name = req_dict.get('name')
        if len(req_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(req_dict.get('id'), req_dict.get('name')))
    except:
        print("Not a valid JSON")
