#!/usr/bin/python3
""" 4-json_api.py - send user input in a POST request & receives JSON data """

if __name__ == "__main__":

    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    params = {}

    if len(sys.argv) == 1:
        params['q'] = ''
    elif len(sys.argv) == 2:
        params = {'q': sys.argv[1]}
    else:
        print("Usage: [URL] | [URL] [POST value]")
        sys.exit(0)

    # print("my params: {}".format(params))

    r = requests.post(url, data=params)

    try:
        resp = r.json()
        # print("my status code: {}".format(r.status_code))
        if r.status_code == 200:  # Valid JSON
            print("[{}] {}".format(resp['id'], resp['name']))
        elif r.status_code == 204:  # Empty JSON
            print("No result")
        else:  # Invalid JSON
            print("Not a valid JSON")
    except Exception as e:
        print("Not a valid JSON")
