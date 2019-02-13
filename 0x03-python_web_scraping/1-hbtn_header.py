#!/usr/bin/python3
""" 1-hbtn_header.py """

if __name__ == "__main__":

    import requests
    import sys

    if len(sys.argv) == 2:
        url = sys.argv[1]
        try:
            r = requests.get(url)
            print("{}".format(r.headers['x-request-id']))
        except Exception as e:
            print('******Error: ', e)
    else:
        print("Please enter a valid URL")
