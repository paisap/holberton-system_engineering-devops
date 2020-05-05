#!/usr/bin/python3
"""  Export to CSV  """
import csv
import json
import requests
import sys

if __name__ == "__main__":
    the_file = "{}.csv".format(sys.argv[1])
    link_2 = "https://jsonplaceholder.typicode.com/todos?userId=" + sys.argv[1]
    x = requests.get("https://jsonplaceholder.typicode.com/users/2").json()
    x = x["username"]
    y = requests.get(link_2).json()
    with open(the_file, "w") as f:
        for i in y:
            f.write('"{}","{}","{}","{}"\n'.format(i["userId"],
                    x, i["completed"], i["title"]))
