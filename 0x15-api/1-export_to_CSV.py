#!/usr/bin/python3
"""
Export to CSV
"""
import csv
import re
import requests
import sys


API = "https://jsonplaceholder.typicode.com"


def export_to_csv(user_id, user_name, todos):
    """
    Function to export to CSV format
    """

    file_name = f"{user_id}.csv"
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            task_completed = "Completed" if todo.get('completed') else "Not Completed"
            writer.writerow([user_id, user_name, task_completed, todo.get('title')])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            user_id = int(sys.argv[1])
            user_res = requests.get(f'{API}/users/{user_id}').json()
            todos_res = requests.get(f'{API}/todos').json()
            user_name = user_res.get('name')
            todos = list(filter(lambda x: x.get('userId') == user_id, todos_res))
            export_to_csv(user_id, user_name, todos)
            print(
                f'Employee {user_name} is done with tasks({len([t for t in todos if t["completed"]])}/{len(todos)}):'
            )
            for todo in todos:
                print(f'\t{todo.get("title")}')
