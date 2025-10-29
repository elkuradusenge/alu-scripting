#!/usr/bin/python3
"""
function that queries the 'Reddit API'
and prints the titles of the first 10 hot posts under given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            # print("OK", end="")
            return
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    except (ValueError, KeyError, requests.RequestException):
        return