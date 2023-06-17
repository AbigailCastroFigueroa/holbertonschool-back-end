#!/usr/bin/python3

import requests
import json
import sys

user_id = sys.argv[1]
url = 'https://jsonplaceholder.typicode.com/user/' + user_id + '/todos'
users = 'https://jsonplaceholder.typicode.com/users?id=' + user_id
data = requests.get(url)
info = data.json()
users_names = requests.get(users)
response = users_names.json()
undone = 0
done = 0
new = []

for item in response:
    username = item['name']

for items in info:
    if items['completed'] is True:
        done += 1
    undone += 1
print(f"Employee {username} is done with tasks ({done}/{undone}):")

for items in info:
    if items['completed'] is True:
        task = items['title']
        print(f"\t {task}")
