#!/usr/bin/python3
"""
Using the reddit's own API
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """returning top ten post titles recursively"""
    global after
    userr_agentt = {'User-Agent': 'api_advanced-project'}
    urll = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parammeterss = {'after': after}
    resultts = requests.get(urll, params=parammeterss, headers=userr_agentt,
                           allow_redirects=False)

    if resultts.status_code == 200:
        aftter_data = resultts.json().get("data").get("after")
        if aftter_data is not None:
            after = aftter_data
            recurse(subreddit, hot_list)
        all_titles = resultts.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
