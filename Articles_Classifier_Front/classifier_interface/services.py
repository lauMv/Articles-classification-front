import urllib

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def generate_request(url, params = {}):
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    response = urllib.request.urlopen(url, params=params)

    if response.status_code == 200:
        return response.read()


def get_all_articles():
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    url = 'http://127.0.0.1:5000/articles'
    response = urllib.request.urlopen(url)
    data = response.read()
    return data


def get_article(id):
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    url = 'http://127.0.0.1:5000/articles/' + str(id)
    response = urllib.request.urlopen(url)
    data = response.read()
    return data
