#!/usr/bin/python3
"""
Returns information about a user's TODO list progress
using a REST API
"""

import requests
from sys import argv


employee_id = argv[1]
# Fetch user data
user = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}/'.format(
        employee_id)).json()
# Fetch TODO data
user_tasks = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        employee_id)).json()
# Extract completed tasks
completed_tasks = [task.get('title')
                   for task in user_tasks if task.get('completed') is True]

print('Employee {} is done with tasks({}/{}):'.format(user.get('name'),
      len(completed_tasks), len(user_tasks)))
for task in completed_tasks:
    print("\t {}".format(task))
