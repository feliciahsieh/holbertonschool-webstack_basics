#!/usr/bin/python3
""" 8-starwars.py - send user data search StarWarsAPI """

if __name__ == "__main__":

    import requests
    import sys

    if len(sys.argv) == 2:
        cnt = 0
        baseurl = "https://swapi.co/api/people/?search="
        url = baseurl + sys.argv[1]

        r = requests.get(url).json()
        print("Number of results: {}".format(r['count']))
        while cnt < r['count']:
            for result in r['results']:
                cnt += 1
                print("{}".format(result['name']))
            if cnt < r['count']:
                url = r['next']
                r = requests.get(url).json()
    else:
        print("Usage: ./8-starwars.py [search string]")
