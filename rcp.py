from flask import Flask, jsonify, json, request
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

@app.route('/headlines/syria')
def headlines_syria():
        title = request.args.get('Title')

        return "i'm the man"

        

if __name__ == '__main__':
       app.run(debug=True)