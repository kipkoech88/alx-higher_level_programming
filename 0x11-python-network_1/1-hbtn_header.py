#!/usr/bin/python3
""" takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id
variable found in the header of the response.
Y """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(dict(response.headers).get('X-Request-Id'))
