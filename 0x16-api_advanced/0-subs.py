#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/himza25)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        print("Output: Non-existing subreddit")
        return 0

    results = response.json().get("data")
    subscribers = results.get("subscribers")
    print("Output: Existing subreddit")
    print(f"Number of subscribers: {subscribers}")

    return subscribers


# Example usage:
subreddit_name = "python"  # Replace with the subreddit you want to check
number_of_subscribers(subreddit_name)
