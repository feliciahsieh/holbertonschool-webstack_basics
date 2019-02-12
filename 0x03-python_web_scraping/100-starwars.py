#!/usr/bin/python3
""" 100-starwars.py - query API for people appearances in starwars movies """

if __name__ == "__main__":

    from requests import get
    from sys import argv

    if len(argv) == 2:
        ppl = []
        cnt = 0
        baseurl = "https://swapi.co/api/people/?search="
        url = baseurl + argv[1]

        r = get(url).json()
        print("Number of results: {}".format(r['count']))
        while cnt < r['count']:
            for result in r['results']:
                cnt += 1
                print("{}".format(result['name']))
                for movieURL in result['films']:
                    movieRequest = get(movieURL).json()
                    print("\t{}".format(movieRequest['title']))
            if cnt < r['count']:
                url = r['next']
                r = get(url).json()
    else:
        print("Usage: ./8-starwars.py [search string]")
