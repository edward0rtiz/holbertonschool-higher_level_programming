#!/usr/bin/python3
"""script that takes in a string and sends a search request to the SW API"""

import requests
import sys

if __name__ == '__main__':

    url = "https://swapi.co/api/people"
    params = {"search": sys.argv[1]}
    result = requests.get(url, params=params).json()
    print("Number of results: {}".format(result.get("count")))
    [print(req.get("name")) for req in result.get("results")]
