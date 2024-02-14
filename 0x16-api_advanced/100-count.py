#!/usr/bin/python3
"""
A function that help queries the Reddit's API and then prints out
the ten top most hottest posts of the a subreddit
"""
import re
import requests



def add_title(dictionary, hot_posts):
    """ Adding to the list an itemm """
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for wordd in title:
        for keyy in dictionary.keys():
            x = re.compile("^{}$".format(keyy), re.I)
            if x.findall(wordd):
                dictionary[keyy] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """ The queries thats of the Reddit API """
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list, dictionary=None):
    """ A function FOR THE INIT"""
    if dictionary is None:
        dictionary = {}

    for wordd in word_list:
        wordd = wordd.lower()
        if wordd not in dictionary:
            dictionary[wordd] = 0

    recurse(subreddit, dictionary)

    sorted_items = sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0]))
    for itemm in sorted_items:
        if itemm[1] > 0:
            print("{}: {}".format(itemm[0], itemm[1]))
