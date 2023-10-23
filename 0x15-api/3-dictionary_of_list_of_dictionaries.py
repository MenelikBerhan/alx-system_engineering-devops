#!/usr/bin/python3
"""Script that, using this [REST API]('https://jsonplaceholder.typicode.com/')
export data about all users tasks in a json format
to a file named todo_all_employees.json"""

if __name__ == '__main__':
    import json
    import requests

    url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(url=url).json()
    users_list = []
    for user in users:
        users_list.append({'id': user.get('id'),
                           'username': user.get('username')})
    # print(users_list)
    task_url = 'https://jsonplaceholder.typicode.com/todos'
    json_dict = {}
    for usr in users_list:
        task_list = []
        # print(task_url)
        params = {'userId': usr.get('id')}
        tasks = requests.get(url=task_url).json()
        for task in tasks:
            task_list.append({'username': usr['username'],
                              'task': task.get('title'),
                              'completed': task.get('completed')})
        json_dict.update({usr['id']: task_list})
    # print(json_dict[1])
    with open('todo_all_employees.json', 'w') as file:
        json.dump(json_dict, file)
