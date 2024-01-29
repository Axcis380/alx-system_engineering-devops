#!/usr/bin/python3
"""
A Python script to export tasks of all employees to a JSON file.
"""

import json
import requests


def main():
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    users_response = requests.get(users_url)
    users = users_response.json()

    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    user_task_dict = {}

    for user in users:
        user_id = user['id']
        user_task_dict[user_id] = [
            {"username": user['username'],
             "task": task['title'],
             "completed": task['completed']}
            for task in todos if task['userId'] == user_id
        ]

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(user_task_dict, jsonfile)


if __name__ == "__main__":
    main()
