#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """The function to gather data"""
    base_url = f"""
    https://jsonplaceholder.typicode.com/users/{employee_id}/todos
    """

    try:
        response = requests.get(base_url)
        response.raise_for_status()
        todos = response.json()

        # Fetch employee name
        user_info = requests.get(f"""
            https://jsonplaceholder.typicode.com/users/{employee_id}
            """)
        user_info.raise_for_status()
        employee_name = user_info.json()['name']

        # Count completed tasks and fetch task titles
        completed_tasks = [todo['title'] for
                           todo in todos if todo['completed']]
        number_of_done_tasks = len(completed_tasks)
        total_number_of_tasks = len(todos)

        # Display progress
        print(f"Employee {employee_name} is
              done with tasks({number_of_done_
                              tasks}/{total_number_of_tasks}): ")
        print(f"{employee_name}:")

        # Display completed task titles
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
