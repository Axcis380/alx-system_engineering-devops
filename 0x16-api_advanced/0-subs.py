import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
    "User-Agent": "linux:mon_bot_reddit:1.0.0:/u/axcis380"
}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    results = response.json().get("data")
    return results.get("subscribers")
