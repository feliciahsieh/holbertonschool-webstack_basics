#!/usr/bin/python3
""" 4-json_api.py - send user input in a POST request & receives JSON data """

if __name__ == "__main__":

    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    params = {}

    if len(sys.argv) == 1:
        params['q'] = ""
    elif len(sys.argv) == 2 and len(sys.argv[1]) == 1:
        params = {'q': sys.argv[1]}
    else:
        print("Usage: ./4-json_api.py [character]")
        sys.exit(0)

    try:
        r = requests.post(url, data=params)
        resp = r.json()
        if resp == {}:
            print("No result")
            sys.exit(0)
        if r.status_code == 200:  # Valid JSON
            print("[{}] {}".format(resp['id'], resp['name']))
        else:  # Invalid JSON
            print("Not a valid JSON")
    except Exception as e:
            print("Not a valid JSON")
