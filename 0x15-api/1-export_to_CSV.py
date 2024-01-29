#!/usr/bin/python3
"""
A Python script to export TODO list data to a CSV file for a given employee ID.
"""

import csv
import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee ID>")
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

        with open(f'{employee_id}.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in todos:
                writer.writerow([employee_id, user['username'],
                                 task['completed'], task['title']])

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
