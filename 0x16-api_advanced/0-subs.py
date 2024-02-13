#!/usr/bin/python3
"""Function thats to the query of subscribers on a particular
given in Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returning the total number of the subscribers on that given
    subreddit."""
    urll = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headders = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(urll, headders=headders, allow_redirects=False)
    if response.status_code == 404:
        return 0
    resullts = response.json().get("data")
    return resullts.get("subscribers")
