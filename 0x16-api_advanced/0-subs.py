#!/usr/bin/python3
"""Function thats to the query of subscribers on a particular
given in Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returning the total number of the subscribers on that given
    subreddit."""
    urll = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    respn = requests.get(urll, headers=headers, allow_redirects=False)
    if respn.status_code == 404:
        return 0
    resullts = respn.json().get("data")
    return resullts.get("subscribers")
