#!/usr/bin/python3
"""Script that, using this [REST API]('https://jsonplaceholder.typicode.com/'),
for a given employee ID, export data about tasks in a json format
to a file USER_ID.json"""

if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    if len(argv) == 1:
        print('Employee ID not given!')
        exit(1)
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    id = argv[1]
    username = requests.get(url=url).json().get('username')
    tasks = requests.get(url=url + '/todos').json()
    task_list = []
    for task in tasks:
        task_list.append({'task': task.get('title'),
                          'completed': task.get('completed'),
                          'username': username})
    json_dict = {id: task_list}
    with open(id + '.json', 'w') as file:
        json.dump(json_dict, file)
