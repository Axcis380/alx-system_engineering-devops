#!/usr/bin/python3
"""Module to query Reddit API for the top ten hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'MyRedditApp/0.1 (by /u/himza25)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            posts = response.json()['data']['children']
            for post in posts:
                print(post['data']['title'])
        except (KeyError, ValueError):
            print("None")
    else:
        print("None")
