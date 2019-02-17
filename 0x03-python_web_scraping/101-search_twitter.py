#!/usr/bin/python3
""" 101-search_twitter.py -  """

import base64
from requests import get, post
from sys import argv

"""
$ curl --request GET
 --url 'https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular'
 --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app",
 oauth_nonce="generated-nonce", oauth_signature="generated-signature",
 oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp",
 oauth_token="access-token-for-authed-user", oauth_version="1.0"'
"""

if __name__ == "__main__":

    if len(argv) == 4:
        urlPost = "https://api.twitter.com/oauth2/token HTTP/1.1/"
        baseURL = "https://api.twitter.com/1.1/search/tweets.json/"
        apiKey = argv[1]
        apiSecret = argv[2]
        apiSearch = argv[3]

        authText = apiKey + ':' + apiSecret
        encoded = base64.b64encode(authText.encode('ascii'))

        header = {}
        header['Authorization'] = 'Basic '.encode('ascii') + encoded
        header['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8'
        bodytext = 'grant_type=client_credentials'

        param = {}
        param['q'] = '@feliciahsiehsw'
        param['count'] = 5
        r = post(urlPost, data=param, headers=header)
        print(r.text)
        # r = get(baseURL_auth, params=param))
        # rj = r.json()
        # try:
        #    print("rj: {}".format(rjson.text))
        #    id = rj['statuses']['id_str']
        #     tweetText = rj['statuses']['text']
        #     name = rj['statuses']['user']['name']
        #     print("[{}]] {} by {}".format(id, tweetText, name))
        # except Exception as e:
        #    print('None')
    else:
        print("Usage: ./101-search_twitter.py [API Key] [API Secret] [Search]")
