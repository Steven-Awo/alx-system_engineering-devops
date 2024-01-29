#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a
given employee ID, returns information about
his/her TODO list progress.
"""

import requests

from sys import argv

if __name__ == "__main__":

    sessionReq = requests.Session()

    Emplye_id = argv[1]
    URL_id = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(Emplye_id)
    name_of_URL = 'https://jsonplaceholder.typicode.com/users/{}'.format(Emplye_id)

    emplye = sessionReq.get(URL_id)
    name_of_emplye = sessionReq.get(name_of_URL)

    json_requts = emplye.json()
    name = name_of_emplye.json()['name']

    total_numb_of_tasks = 0
    tasks_donne = []
    for tasks_that_has_been_done in json_requts:
        if tasks_that_has_been_done['completed']:
            tasks_donne.append(total_numb_of_tasks)
            total_numb_of_tasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, total_numb_of_tasks, len(json_requts)))

    for tasks_that_has_been_done in json_requts:
        if tasks_that_has_been_done['completed']:
            print("\t " + tasks_that_has_been_done.get('title'))
