#!/usr/bin/python3
"""  Top Ten """
import json
import requests


def top_ten(subreddit):
    """  titles of the first 10 hot posts """
    link = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    try:
        x = requests.get(link, headers={'User-Agent': 'Santiago'}).json()
        aux = (x.get('data').get("children"))
        for i in aux:
            print(i.get("data").get("title"))
    except:
        print('None')
