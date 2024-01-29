#!/usr_name/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the CSV format.
"""

import requests

import json

import csv

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

    total_numb_of_tasks = 0

    for done_tasks in json_requts:
        if done_tasks['completed']:
            total_numb_of_tasks += 1

    file_CSV = Emplye_id + '.csv'

    with open(file_CSV, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for x in json_requts:
            write.writerow([Emplye_id, usr_name, x.get('completed'), x.get('title')])
