#!/usr/bin/python3
""" 0-hbtn_status.py """

if __name__ == "__main__":

    import requests

    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
