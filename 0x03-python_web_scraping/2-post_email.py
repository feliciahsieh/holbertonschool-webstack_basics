#!/usr/bin/python3
""" 2-post_email.py - send POST to url with email and print result """

if __name__ == "__main__":

    import requests
    import sys

    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        payload = {'email': email}
        r = requests.post(url, data=payload)
        print("{}".format(r.text))
    else:
        print("Please enter a valid URL and email")
