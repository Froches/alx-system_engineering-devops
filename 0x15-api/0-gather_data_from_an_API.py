#!/usr/bin/python3
"""
Module to gather employee data
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    # Base URL
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user = requests.get(url + f"users/{employee_id}").json()

    # Fetch todos for the user
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    # Calculate progress
    completed_tasks = [task for task in todos if task.get('completed') is True]
    total_tasks = len(todos)

    print(
        f"Employee {user.get('name')} is done with tasks("
        f"{len(completed_tasks)}/{total_tasks}):"
    )
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))


# Usage: python script.py [EMPLOYEE_ID]
if __name__ == "__main__":
    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
