#!/usr/bin/python3
"""Module containing a function that prints hot posts of a given subreddit"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a given subreddit
    If an invalid subreddit is given, prints 'None'."""

    headers = {"User-Agent": "Menelik Berhan"}

    # search given subreddit
    params = {"raw_json": 1, 'query': subreddit, 'exact': True,
              'include_unadvertisable': True}
    url = "https://www.reddit.com/api/search_subreddits.json"
    response = requests.post(url=url, headers=headers, params=params)

    # if found get and print top ten posts, else print None
    if response.status_code == 200:
        params = {'limit': 10}
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        response = requests.get(url, headers=headers, params=params)
        posts = response.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    else:
        print(None)
