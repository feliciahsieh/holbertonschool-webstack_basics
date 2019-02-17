#!/usr/bin/python3
""" 7-github_commits.py - print user's last 10 Github commits """
import requests
import sys

if __name__ == "__main__":

    baseurl = "https://api.github.com/repos/"
    nameRepo = sys.argv[1]
    nameUser = sys.argv[2]

    url = baseurl + nameUser + '/' + nameRepo + '/commits'
    try:
        r = requests.get(url).json()
        for i in range(10):
            print("{}: {}".format(
                r[i]['sha'], r[i]['commit']['author']['name']))
    except Exception as e:
        pass
