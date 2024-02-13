#!/usr/bin/python3
"""
Using the reddit's own API
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """returning top ten post titles recursively"""
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    urll = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parammeterss = {'after': after}
    results = requests.get(urll, params=parammeterss, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        aftter_data = results.json().get("data").get("after")
        if aftter_data is not None:
            after = aftter_data
            recurse(subreddit, hot_list)
        all_the_titles = results.json().get("data").get("children")
        for tittle_r in all_the_titles:
            hot_list.append(tittle_r.get("data").get("title"))
        return hot_list
    else:
        return (None)
