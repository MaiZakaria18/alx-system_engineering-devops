#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv


if __name__ == "__main__":
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))

    user_data = user.json()
    todos_data = todos.json()
    TOTAL_NUMBER_OF_TASKS = len(todos_data)
    NUMBER_OF_DONE_TASKS = 0
    completed_tasks = []
    for task in todos_data:
        if task["completed"] is True:
            completed_tasks.append(task["title"])
            NUMBER_OF_DONE_TASKS += 1
    print("Employee {} is done with tasks({}/{}):".format(
        user_data["name"], NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in completed_tasks:
        print("\t {}".format(task))
