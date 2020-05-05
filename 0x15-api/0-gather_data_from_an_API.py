#!/usr/bin/python3
""" Gather data from an API """
import json
import requests
import sys

if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    link_2 = "https://jsonplaceholder.typicode.com/todos?userId=" + sys.argv[1]
    x = requests.get(link).json()
    y = requests.get(link_2).json()
    tasks = []
    count = 0
    for i in y:
        if i["completed"] is True:
            tasks.append(i["title"])
        count += 1
    print("Employee {} is done with tasks({}/{}):".format(x["name"],
          len(tasks), count))
    for i in tasks:
        print("\t {}".format(i))
