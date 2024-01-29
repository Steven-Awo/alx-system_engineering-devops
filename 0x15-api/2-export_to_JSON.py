#!/usr/bin/python3
"""
Write a Python script that, Using what you did in the
task #0, extend your Python script to export
data in the JSON format.
"""
import json

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
    usr_name = name_of_emplye.json()['username']
    
    total_numb_of_Tasks = []
    updating_the_User = {}

    for all_the_Empl in json_requts:
        total_numb_of_Tasks.append(
            {
                "task": all_the_Empl.get('title'),
                "completed": all_the_Empl.get('completed'),
                "username": usr_name,
            })
    updating_the_User[Emplye_id] = total_numb_of_Tasks

    file_of_Json = Emplye_id + ".json"
    with open(file_of_Json, 'w') as f:
        json.dump(updating_the_User, f)
