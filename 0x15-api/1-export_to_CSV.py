#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the CSV format.
"""

import requests
import sys


if __name__ == '__main__':
    emplooy_Id = sys.argv[1]
    Url_id = "https://jsonplaceholder.typicode.com/users"
    url_name = Url_id + "/" + emplooy_Id

    respns = requests.get(url_name)
    usr_name = respns.json().get('usr_name')

    todos_Url = url_name + "/todos"
    respns = requests.get(todos_Url)
    tasks_to_do = respns.json()

    with open('{}.csv'.format(emplooy_Id), 'w') as file:
        for task_did in tasks_to_do:
            file.write('"{}","{}","{}","{}"\n'
                       .format(emplooy_Id, usr_name, task_did.get('completed'),
                               task_did.get('title')))
