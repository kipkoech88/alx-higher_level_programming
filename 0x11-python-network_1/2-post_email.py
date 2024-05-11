#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    val = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(val).encode('ascii')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        """Display body of the response"""
        print(response.read().decode('utf8'))
