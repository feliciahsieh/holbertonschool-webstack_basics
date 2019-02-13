#!/usr/bin/python3
""" 0-hbtn_status.py """

if __name__ == "__main__":

    import requests

    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)

    print("Body response:")
    print("- type: {}".format(type(r.text)))
    print("- content: {}".format(r.text))
