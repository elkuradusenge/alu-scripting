#!/usr/bin/python3
"""
Fetchs number of subscribers from a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ Set a customized header user-agent """
    headers = {"User-Agent": "ALU-scripting"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    try:
        response = requests.get(url, allow_redirects=False)
    except requests.exceptions.RequestException:
        return 0

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0
