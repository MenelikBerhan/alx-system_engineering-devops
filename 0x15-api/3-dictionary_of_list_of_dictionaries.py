#!/usr/bin/python3
"""Script that, using this [REST API]('https://jsonplaceholder.typicode.com/')
export data about all users tasks in a json format
to a file named todo_all_employees.json"""

if __name__ == '__main__':
    import json
    import requests

    url = "https://jsonplaceholder.typicode.com/users"
    res = requests.get(url)
    users = res.json()
    res.close()
    users_list = []
    for user in users:
        users_list.append({'id': user.get('id'),
                           'username': user.get('username')})
    task_url = "https://jsonplaceholder.typicode.com/todos"
    json_dict = {}
    for usr in users_list:
        task_list = []
        params = {'userId': str(usr.get('id'))}
        res = requests.get(task_url, params=params)
        tasks = res.json()
        res.close()
        for task in tasks:
            task_list.append({'username': usr['username'],
                              'task': task.get('title'),
                              'completed': task.get('completed')})
        json_dict.update({usr.get('id'): task_list})

    with open('todo_all_employees.json', 'w') as file:
        json.dump(json_dict, file)
