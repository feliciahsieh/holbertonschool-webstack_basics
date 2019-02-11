#!/usr/bin/python3
""" 6-my_github.py - print user's github id w/ username:pwd from cmd line """

import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) == 3:
        baseurl = "https://api.github.com/user"
        username = sys.argv[1]
        password = sys.argv[2]

        r = requests.get(baseurl, auth=(username, password))
        rjson = r.json()
        try:
            print(rjson['id'])
        except Exception as e:
            print('None')
    else:
        print("Usage: ./6-my_github.py [username] [password]")
