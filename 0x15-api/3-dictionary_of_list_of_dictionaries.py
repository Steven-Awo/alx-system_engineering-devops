#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""

import json

import requests

if __name__ == "__main__":

    import json

    import requests

    userss = requests.get("https://jsonplaceholder.typicode.com/users")
    userss = userss.json()
    toddos = requests.get('https://jsonplaceholder.typicode.com/todos')
    toddos = toddos.json()
    toddo_all = {}

    for usrr in userss:
        the_List_of_task = []
        for taskk in toddos:
            if taskk.get('userId') == usrr.get('id'):
                the_task_Dict = {"username": usrr.get('username'),
                            "task": taskk.get('title'),
                            "completed": taskk.get('completed')}
                the_List_of_task.append(the_task_Dict)
        toddo_all[usrr.get('id')] = the_List_of_task

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(toddo_all, f)
