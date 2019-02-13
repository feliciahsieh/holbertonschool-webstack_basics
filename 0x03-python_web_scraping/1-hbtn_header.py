#!/usr/bin/python3
""" 1-hbtn_header.py """

if __name__ == "__main__":

    from requests import get
    from sys import argv

    if len(argv) == 2:
        url = argv[1]
        try:
            r = get(url)
            print("{}".format(r.headers.get('x-request-id')))
        except Exception as e:
            print('******Error: ', e)
    else:
        print("Please enter a valid URL")
