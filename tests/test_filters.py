import pytest
import requests
import json

def test_filter_status_code():
    response = requests.get('http://127.0.0.1:5000/headlines?title=Trump')
    assert response.status_code == 200

def test_filter_content():
    response = requests.get('http://127.0.0.1:5000/headlines?title=Trump')
    content = response.content
    headlines = json.loads(content)
    assert type(content[1]) == str