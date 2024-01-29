#!/usr/bin/python3
"""
Write a Python script that, using what you did in the task
#0, extend your Python script to export data in
the CSV format.
"""

import requests

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
    name = name_of_emplye.json()['name']

    total_numb_of_tasks = 0

    for tasks_that_has_been_done in json_requts:
        if tasks_that_has_been_done['completed']:
            total_numb_of_tasks += 1

    filee_CSV = Emplye_id + '.csv'

    with open(filee_CSV, "w", newline='') as csv_file:
        write = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        for x in json_requts:
            write.writerow([Emplye_id, usr, x.get('completed'), x.get('title')])

    # print("Employee {} is done with tasks({}/{}):".
    #       format(name, total_numb_of_tasks, len(json_requts)))

    # for tasks_that_has_been_done in json_requts:
    #     if tasks_that_has_been_done['completed']:
    #         print("\t " + tasks_that_has_been_done.get('title'))
