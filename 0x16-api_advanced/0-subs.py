import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if not isinstance(subreddit, str):
        return 0
    
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced:v1.0.0 (by /u/firdaus_cartoon_jr)'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except requests.exceptions.HTTPError as e:
        # If subreddit is invalid or other HTTP error occurs, return 0
        return 0
    except KeyError as e:
        # If the JSON structure is unexpected, return 0
        return 0
