#!/usr/bin/python3
"""Module containing a function that returns hot posts of a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], subreddit_checked=False, after=None):
    """returns a list containing the titles of all hot articles for a given
    subreddit. If an invalid subreddit is given, returns 'None'."""

    headers = {"User-Agent": "Menelik Berhan"}
    if not subreddit_checked:
        # search given subreddit
        params = {"raw_json": 1, 'query': subreddit, 'exact': True,
                  'include_unadvertisable': True}
        url = "https://www.reddit.com/api/search_subreddits.json"
        response = requests.post(url=url, headers=headers, params=params)
        subreddit_exists = response.status_code == 200
    else:
        subreddit_exists = True

    # if found get and print top ten posts, else print None
    if subreddit_exists:
        if after is None:
            params = {'limit': 50}
        else:
            params = {'limit': 50, 'after': after}
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        response = requests.get(url, headers=headers, params=params)
        resp = response.json().get('data')
        if resp.get('children'):
            for post in resp.get('children'):
                hot_list.append(post.get('data').get('title'))
        else:
            return (hot_list)
        if resp.get('after') is None:
            return (hot_list)
        else:
            return (recurse(subreddit, hot_list, True,
                            after=resp.get('after')))
    else:
        return (None)
