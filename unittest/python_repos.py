import requests


def send_request():
    """Make an API call and return the response information."""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    return r.status_code

def search_github():
    """Call the fuction send_request()."""
    return send_request()
