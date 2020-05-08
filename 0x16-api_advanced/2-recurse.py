#!/usr/bin/python3
"""   Recurse it """
import json
import requests


def recurse(subreddit, hot_list=[], after=''):
    """ curssion """
    if after is None:
        return hot_list

    link = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                  after)
    x = requests.get(link, headers={'User-Agent': 'Santiago'}).json()

    if 'error' in x:
        return None

    for post in x.get('data').get('children'):
        hot_list.append(post.get('data').get('title'))
    siguiente = x.get('data').get('after')
    return recurse(subreddit, hot_list, siguiente)
