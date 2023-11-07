#!/usr/bin/python3
"""func to print posts"""
import requests


def top_ten(subreddit):
    """func to print the titles of 10 hottest posts"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print("None")
        return

    res = response.json().get("data")

    [print(c.get("data").get("title")) for c in res.get("children")]
