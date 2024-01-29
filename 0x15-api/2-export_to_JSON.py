#!/usr/bin/python3
"""
A Python script designed to export TODO list information to a JSON file, with a specified employee ID as the input.
"""

import json
import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee ID>")
        return

    employee_id = sys.argv[1]
    try:
        user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        todos_url = ('https://jsonplaceholder.typicode.com/todos'
                     f'?userId={employee_id}')

        user_response = requests.get(user_url)
        user = user_response.json()

        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        tasks = [{"task": task["title"],
                  "completed": task["completed"],
                  "username": user["username"]} for task in todos]

        tasks_dict = {employee_id: tasks}

        with open(f'{employee_id}.json', 'w') as jsonfile:
            json.dump(tasks_dict, jsonfile)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
