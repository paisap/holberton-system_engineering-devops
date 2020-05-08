#!/usr/bin/python3
import requests
import json


def number_of_subscribers(subreddit):
    link = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
    try:
        x = requests.get(link, headers={'User-Agent': 'Santiago'}).json()
        return (x.get('data').get('subscribers'))
    except:
        return 0
