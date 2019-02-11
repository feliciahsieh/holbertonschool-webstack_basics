#!/usr/bin/python3
""" 7-github_commits.py - print user's last 10 Github commits """

import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) == 3:
        baseurl = "https://api.github.com/repos/"
        nameRepo = sys.argv[1]
        nameUser = sys.argv[2]

        url = baseurl + nameUser + '/' + nameRepo + '/commits'
        r = requests.get(url)
        rjson = r.json()
        try:
            for i in range(10):
                print("{}: {}".format(
                    rjson[i]['sha'], rjson[i]['commit']['author']['name']))
        except Exception as e:
            print('Not found')
    else:
        print("Usage: ./7-github_commits.py [username] [repo name]")
