from flask import Flask, jsonify, json
import requests 
import json

app = Flask(__name__)

@app.route('/')
def home():
    return ('Hello, Biatch!')

@app.route('/headlines')
def send_headlines():
    data_file = 'headlines.json'
    with open(data_file) as f:
        headlines = json.load(f)
        return jsonify(headlines)

url = 'http://127.0.0.1:5000/headlines/country'
headers = {'Content-Type': 'application/json'}

filters = [dict(name='Title', op='==', val='%Syria%')]
params = dict(q=json.dumps(dict(filters=filters)))

response = requests.get(url, params=params, headers=headers)
assert response.status_code == 200
print(response.json())

if __name__ == '__main__':
       app.run(debug=True)