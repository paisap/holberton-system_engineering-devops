#!/usr/bin/python3
""" Export to JSON """
import json
import requests
import sys

if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com/users"
    link_1 = "https://jsonplaceholder.typicode.com/todos"
    users = requests.get(link).json()
    alls = requests.get(link_1).json()
    the_file = "todo_all_employees.json"
    dict_1 = {}
    for user in users:
        tasks = []
        for task in alls:
            if task["userId"] == user["id"]:
                dictionary = {}
                dictionary["task"] = task.get("title")
                dictionary["completed"] = task.get("completed")
                dictionary["username"] = user.get("username")
                tasks.append(dictionary)
        dict_1[user["id"]] = tasks
    with open(the_file, "w") as f:
        json.dump(dict_1, f)
