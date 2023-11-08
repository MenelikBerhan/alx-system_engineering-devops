#!/usr/bin/python3
"""Module containing a function that parses the title of all hot articles,
and prints a sorted count of given keywords"""
import requests


def count_words(subreddit, word_list, hot_list={}, subreddit_checked=False,
                after=None):
    """parses the title of all hot articles, and prints a sorted count of
    given keywords (case-insensitive, delimited by spaces). If no posts match
    or the subreddit is invalid, prints nothing."""

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
            params = {'limit': 100}
        else:
            params = {'limit': 100, 'after': after}
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        response = requests.get(url, headers=headers, params=params)
        resp = response.json().get('data')
        if not resp.get('children'):
            sorted_keys = list(hot_list.keys()).sort()
            sorted_keys.sort(key=lambda x: hot_list[x], reverse=True)
            for key in sorted_keys:
                print('{}: {}'.format(key, hot_list[key]))
                exit(0)

        words = [word.lower() for word in word_list]
        for post in resp.get('children'):
            title = str(post.get('data').get('title'))
            title_list = title.lower().split()
            for word in words:
                word_count = title_list.count(word)
                if word_count:
                    hot_list[word] = hot_list.get(word, 0) + word_count

        count_words(subreddit, word_list, hot_list, True,
                    after=resp.get('after'))
