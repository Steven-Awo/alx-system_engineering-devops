#!/usr/bin/python3
"""
Using the reddit's own API
"""
import requests
after = None


def recurse(subreddit, hottest_list=[]):
    """returning top ten post titles recursively"""
    global after
    userr_agentt = {'User-Agent': 'api_advanced-project'}
    urll = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    resultts = requests.get(urll, params=parameters, headers=userr_agentt,
                           allow_redirects=False)

    if resultts.status_code == 200:
        aftter_data = resultts.json().get("data").get("after")
        if aftter_data is not None:
            after = aftter_data
            recurse(subreddit, hottest_list)
        all_the_titles = resultts.json().get("data").get("children")
        for tittle_r in all_the_titles:
            hottest_list.append(tittle_r.get("data").get("title"))
        return hottest_list
    else:
        return (None)
