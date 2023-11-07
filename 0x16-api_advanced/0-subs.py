#!/usr/bin/python3
"""func to query subscribers"""
import requests


def number_of_subscribers(subreddit):
    """func to count the total number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    res = response.json().get("data")
    return res.get("subscribers")
