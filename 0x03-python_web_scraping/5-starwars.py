#!/usr/bin/python3
""" 5-starwars.py - send user data as search request to StarWarsAPI """

if __name__ == "__main__":

    import requests
    import sys

    if len(sys.argv) == 2:
        baseurl = "https://swapi.co/api/people/?search="
        url = baseurl + sys.argv[1]
        r = requests.get(url)
        rjson = r.json()

        print("Number of results: {}".format(rjson['count']))
        for result in rjson['results']:
            print("{}".format(result['name']))
    else:
        print("Usage: ./5-starwars.py [search string]")
