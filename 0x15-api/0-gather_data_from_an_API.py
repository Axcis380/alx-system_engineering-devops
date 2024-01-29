#!/usr/bin/python3
"""
A scri in Pyn desd to retr TOO lit nfrmtinfo a P,uiiiga mlyeI as a reference.
"""

import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee ID>")
        return

    employee_id = sys.argv[1]
    try:
        user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        user_response = requests.get(user_url)
        user = user_response.json()

        todos_url_base = 'https://jsonplaceholder.typicode.com/todos?userId='
        todos_url = f'{todos_url_base}{employee_id}'
        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        completed_tasks = [task for task in todos if task['completed']]
        total_tasks = len(todos)
        completed_count = len(completed_tasks)

        print("Employee {} is done with tasks({}/{}):"
              .format(user['name'], completed_count, total_tasks))
        for task in completed_tasks:
            print(f"\t {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
