#!/usr/bin/python3
"""Module containing a function that parses the title of all hot articles,
and prints a sorted count of given keywords"""
import requests


def count_words(subreddit, word_list, word_dict={}, after=None):
    """parses the title of all hot articles, and prints a sorted count of
    given keywords (case-insensitive, delimited by spaces). If no posts match
    or the subreddit is invalid, prints nothing."""

    headers = {"User-Agent": "Menelik Berhan"}
    params = {'after': after}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return (None)

    resp = response.json().get('data')
    if not resp.get('children'):
        return (None)

    words = [word.lower() for word in word_list]
    for post in resp.get('children'):
        title = str(post.get('data').get('title'))
        title_list = title.lower().split()
        for word in words:
            word_count = title_list.count(word)
            if word_count:
                word_dict[word] = word_dict.get(word, 0) + word_count

    if not resp.get('after'):
        sorted_keys = list(word_dict.keys()).sort()
        sorted_keys.sort(key=lambda x: word_dict[x], reverse=True)
        for key in sorted_keys:
            print('{}: {}'.format(key, word_dict[key]))
    else:
        return (count_words(subreddit, word_list, word_dict,
                            after=resp.get('after')))
