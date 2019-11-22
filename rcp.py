from flask import Flask
from flask import url_for
from flask import jsonify
import json


app = Flask(__name__)

@app.route('/')
def home():
    return ('Hello, Biatch!')

@app.route('/headlines')
def headlines_api():
       headlines = 'headlines.json'
       return jsonify([headline for headline in headlines])

if __name__ == '__main__':
    app.run(debug=True)