import pytest
import requests
from flask import Flask, jsonify

def test_get():
    response = requests.get('http://127.0.0.1:5000/headlines/all')
    assert response.status_code == 200




# # This would be testing the app
# def test_json():
#     response = requests.get('http://127.0.0.1:5000/headlines/all')
#     json_response = jsonify(response)
#     assert json_response.content_type == 'application/json'

