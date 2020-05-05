#!/usr/bin/python3
""" Export to JSON """
import json
import requests
import sys

if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    link_2 = "https://jsonplaceholder.typicode.com/todos?userId=" + sys.argv[1]
    x = requests.get(link).json()
    y = requests.get(link_2).json()
    lista = []
    dict_1 = {}
    the_file = "{}.json".format(sys.argv[1])
    for i in y:
        dictionary = {}
        dictionary["task"] = i["title"]
        dictionary["completed"] = i["completed"]
        dictionary["username"] = x["username"]
        lista.append(dictionary)
    dict_1[sys.argv[1]] = lista
    with open(the_file, "w") as f:
        json.dump(dict_1, f)
