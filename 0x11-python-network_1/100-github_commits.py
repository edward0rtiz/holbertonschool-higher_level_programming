#!/usr/bin/python3
"""Retrieve 10 first commit sorted on rails repo from user rails"""

import requests
import sys

if __name__ == '__main__':

    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[1], sys.argv[2])
    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get('sha'),
                                  commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
