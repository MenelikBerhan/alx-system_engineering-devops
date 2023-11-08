#!/usr/bin/python3
"""Module containing a function that parses the title of all hot articles,
and prints a sorted count of given keywords"""
import requests


def count_words(subreddit, word_list, count=None, after=None):
    """parses the title of all hot articles, and prints a sorted count of
    given keywords (case-insensitive, delimited by spaces). If no posts match
    or the subreddit is invalid, prints nothing."""
    if count is None:
        count = {}

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    header = {'User-agent': 'ALX project'}
    if after:
        url += "&after={}".format(after)
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']

    if not posts:
        return count

    words = [w.lower() for w in word_list]
    for post in posts:
        title = str(post.get('data').get('title'))
        title_list = title.lower().split()
        for word in words:
            wrd_count = title_list.count(word)
            if wrd_count:
                count[word] = count.get(word, 0) + wrd_count

    after = data['data']['after']
    if after:
        return count_words(subreddit, word_list, count, after)
    count_keys = list(count.keys())
    if count_keys:
        count_keys.sort()
        count_keys.sort(key=lambda x: count[x], reverse=True)
    else:
        count_keys = []
    for key in count_keys:
        print("{}: {}".format(key, count[key]))
