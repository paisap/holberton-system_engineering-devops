#!/usr/bin/python3
"""  Export to CSV  """
import csv
import json
import requests
import sys

if __name__ == "__main__":
    the_file = "{}.csv".format(sys.argv[1])
    link = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    link_2 = "https://jsonplaceholder.typicode.com/todos?userId=" + sys.argv[1]
    username = requests.get(link).json()
    data = requests.get(link_2).json()
    get_username = username["username"]
    with open(the_file, "w") as f:
        for i in data:
            f.write('"{}","{}","{}","{}"\n'.format(i["userId"],
                    get_username, i["completed"], i["title"]))
