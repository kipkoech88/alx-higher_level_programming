#!/usr/bin/python3
"""takes repository name
and username to see the commits
by a user to a certain repository"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    username = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(username, repo)

    r = requests.get(url)
    commits = r.json()
    for i in range(10):
        print("{}: {}".format(commits[i].get("sha"),
              commits[i].get("commit").get("author").get("name")))
