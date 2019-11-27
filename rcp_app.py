from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return ('Hello, Biatch!')

@app.route('/headlines/<path:filename>')
def send_headlines(filename):
       headlines = send_from_directory(app.static_folder, 'headlines.json')
       return headlines

if __name__ == '__main__':
       app.run(debug=True)