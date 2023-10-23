#!/usr/bin/python3
"""Script that, using this [REST API]('https://jsonplaceholder.typicode.com/'),
for a given employee ID, export data in a CSV format ("USER_ID","USERNAME",
"TASK_COMPLETED_STATUS","TASK_TITLE" to a file USER_ID.csv"""

if __name__ == '__main__':
    import csv
    import requests
    from sys import argv

    if len(argv) == 1:
        print('Employee ID not given!')
        exit(1)
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    id = argv[1]
    username = requests.get(url=url).json().get('username')
    tasks = requests.get(url=url + '/todos').json()

    with open(id + '.csv', 'w') as csvfile:
        fieldnames = ['id', 'username', 'status', 'title']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='unix')
        base_dict = {'id': id, 'username': username}
        for task in tasks:
            task_dict = {'status': task.get('completed'),
                         'title': task.get('title')}
            task_dict.update(base_dict)
            writer.writerow(task_dict)
