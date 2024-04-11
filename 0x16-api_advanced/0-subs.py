#!/usr/bin/python3
"""How many subs?"""
import requests


def number_of_subscribers(subreddit):
    """
    get number of subscribers
    args:
        subreddit: the name of subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url=url)
    if (response.status_code != 200):
        return 0
    subscribers = response.json()["data"]["subscribers"]
    return (subscribers)

    return sub_info.json().get("data").get("subscribers")
