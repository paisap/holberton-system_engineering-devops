#!/usr/bin/python3
""" Gather data from an API """

import requests
import json
import sys
if __name__ == "__main__":
    x = requests.get("https://jsonplaceholder.typicode.com/users/2").json()
    y = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId=2").json()
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
