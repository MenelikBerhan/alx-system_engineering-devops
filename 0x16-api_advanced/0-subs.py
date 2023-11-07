#!/usr/bin/python3
"""Module containing a function that returns subbredit subscribers count"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function will return 0."""

    headers = {"User-Agent": "Menelik Berhan"}

    # search given subreddit
    params = {"raw_json": 1, 'query': subreddit, 'exact': True,
              'include_unadvertisable': True}
    url = "https://www.reddit.com/api/search_subreddits.json"
    response = requests.post(url=url, headers=headers, params=params)

    # if found get and return subscribers no, else return 0.
    if response.status_code == 200:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        response = requests.get(url, headers=headers)
        return (response.json().get('data').get('subscribers'))
    else:
        return (0)
