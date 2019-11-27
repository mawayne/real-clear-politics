from flask import Flask, jsonify, json

app = Flask(__name__)

@app.route('/')
def home():
    return ('Hello, Biatch!')

@app.route('/headlines')
def send_headlines():
    data_file = 'headlines.json'
    with open(data_file) as f:
        headlines = json.load(f)
        return jsonify(headlines[:10])

if __name__ == '__main__':
       app.run(debug=True)