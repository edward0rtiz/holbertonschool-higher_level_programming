#!/usr/bin/python3
"""script that takes in a string and sends a search request to the SW API"""

import requests
import sys

if __name__ == '__main__':

    url = 'https://swapi.co/api/people'
    params = {'search': sys.argv[1]}
    result = requests.get(url, params=params).json()
    count = result.get('count')
    print("Number of results: {}".format(count))

    page = 0
    while page < count:
        for r in result.get('results'):
            print(r.get('name'))
            page += 1
        next_page = result.get('next')
        if next_page is not None:
            result = requests.get(next_page).json()
