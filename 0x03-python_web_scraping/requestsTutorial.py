#!/usr/bin/python3
""" requestsTutorial.py """

import requests


url = "https://intranet.hbtn.io/status"
r = requests.get(url)

print("r:", r)
print("r.status_code:", r.status_code)
print("r.text:", r.text)
print("r.encoding:", r.encoding)
print("r.raw:", r.raw)
print("r.content:", r.content)

headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print("r: (headers)", r)
print("r.text: (headers)", r.text)
print("r.headers: (headers)", r.headers)
