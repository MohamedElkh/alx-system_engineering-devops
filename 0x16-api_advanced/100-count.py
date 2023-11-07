#!/usr/bin/python3
"""func to contains the count words"""
import requests


def count_words(subreddit, word_list, f_list=[], after=None):
    """func to print counts of given words"""
    user_agent = {'User-agent': 'test45'}

    posts = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                         .format(subreddit, after), headers=user_agent)

    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts.status_code == 200:
        posts = posts.json()['data']
        af = posts['after']
        posts = posts['children']

        for p in posts:
            title = p['data']['title'].lower()

            for word in title.split(' '):
                if word in word_list:
                    f_list.append(word)

        if af is not None:
            count_words(subreddit, word_list, f_list, af)
        else:
            res = {}

            for word in f_list:
                if word.lower() in res.keys():
                    res[word.lower()] += 1
                else:
                    res[word.lower()] = 1

            for key, val in sorted(res.items(), key=lambda item: item[1],
                                   reverse=True):
                print('{} {}'.format(key, val))
    else:
        return
