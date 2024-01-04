#!/usr/bin/python3
"""
Function to gather data from an API
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    The function to get employee todo progress
    """

    try:
        todos = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos').json()
        user_info = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()
        name = user_info['name']
        completed_tasks = [
                todo['title'] for todo in todos if todo['completed']
        ]
        done_tasks = len(completed_tasks)
        total_tasks = len(todos)
        print(f"Employee {name} is done with tasks ({done_tasks}/{total_tasks}):")
        print(f"{name}:")
        for task in completed_tasks:
            print(f"\t{task}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
