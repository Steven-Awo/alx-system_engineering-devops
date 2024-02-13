#!/usr/bin/python3
"""Function thats to print the hot posts on the given Reddit
subreddit."""
import requests


def top_ten(subreddit):
    """Prints out the titles thats of the 10 most hottest
    posts on the a given subreddit."""
    urll = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    respse = requests.get(urll, headers=headers, params=params,
                            allow_redirects=False)
    if respse.status_code == 404:
        print("None")
        return
    resullts = respse.json().get("data")
    [print(c.get("data").get("title")) for c in resullts.get("children")]
