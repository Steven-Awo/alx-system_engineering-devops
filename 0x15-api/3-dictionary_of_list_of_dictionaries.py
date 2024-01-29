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

    userrss = requests.get("https://jsonplaceholder.typicode.com/users")
    userss = userrss.json()
    toddoss = requests.get('https://jsonplaceholder.typicode.com/todos')
    toddos = toddoss.json()
    toddo_all = {}

    for user in userss:
        user_id = str(user.get('id'))
        user_username = user.get('username')
        the_List_of_task = []
        for taskk in toddos:
            if taskk.get('userId') == user_id:
                the_task_Dict = {"username":  user_username,
                            "task": taskk.get('title'),
                            "completed": taskk.get('completed')}
                the_List_of_task.append(the_task_Dict)
        toddo_all[user.get('id')] = the_List_of_task

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(toddo_all, f)
