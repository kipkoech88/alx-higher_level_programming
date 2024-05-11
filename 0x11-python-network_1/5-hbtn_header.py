#!/usr/bin/python3
""" take in URL as arg
and display value of
variable in response
headers """
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
