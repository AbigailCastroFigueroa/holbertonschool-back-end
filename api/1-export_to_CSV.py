#!/usr/bin/python3
"""Script to write a CSV file."""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    userid = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    todo = requests.get(f'{url}/{userid}/todos')
    users = requests.get(f'{url}?id={userid}')
    users_resp = users.json()
    todo_resp = todo.json()

    for user in users_resp:
        username = user['name']

    with open(f'{userid}.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for item in todo_resp:
            status = item['completed']
            task = item['title']
            writer.writerow([userid, username, status, task])
