import pytest
import requests
import json

def test_none():
    response = requests.get('http://127.0.0.1:5000/headlines/all')
    content = response.content
    headlines = json.loads(content)
    for headline in headlines:
        assert headline is not None

def test_url():
    response = requests.get('http://127.0.0.1:5000/headlines/all')
    content = response.content
    headlines = json.loads(content)
    for headline in headlines:
        url = headline['url']
    assert 'https://' in url == True

# def test_date():
#     response = requests.get('http://127.0.0.1:5000/headlines/all')
#     headlines = response.text


        


