#!/usr/bin/python3
""" 3-error_code.py - send HTTP request to URL and check for errors """

if __name__ == "__main__":

    import requests
    import sys

    if len(sys.argv) == 2:
        url = sys.argv[1]
        r = requests.get(url)
        if r.status_code >= 400:
            print("Error code: {}".format(r.status_code))
        else:
            print("{}".format(r.text))
    else:
        print("Please enter a valid URL and email")
