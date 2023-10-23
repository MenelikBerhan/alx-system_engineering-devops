#!/usr/bin/python3
"""Script that, using this [REST API]('https://jsonplaceholder.typicode.com/'),
for a given employee ID, returns information about his/her TODO list status."""

if __name__ == '__main__':
    import requests
    from sys import argv

    if len(argv) == 1:
        print('Employee ID not given!')
        exit(1)
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    name = requests.get(url=url).json()['name']
    total = len(requests.get(url=url + '/todos').json())
    params = {'completed': 'true'}
    completed = requests.get(url=url + '/todos', params=params).json()
    done = len(completed)
    print('Employee {} is done with tasks({}/{}):'.format(name, done, total))
    for td in completed:
        print('\t {}'.format(td['title']))
