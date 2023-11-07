#!/usr/bin/python3
"""func to query the list of all hot posts"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """func to return the list of titles of posts"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    params = {
            "after": after,
            "count": count,
            "limit": 100
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return None

    res = response.json().get("data")
    after = res.get("after")
    count += res.get("dist")

    for c in res.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
