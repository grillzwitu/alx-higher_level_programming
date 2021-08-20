#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL & displays the body of the response
"""


if __name__ == '__main__':
    import requests
    from sys import argv
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
