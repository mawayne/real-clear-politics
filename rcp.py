from flask import Flask
from flask import url_for
from flask import jsonify


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return ('Hello, Biatch!')

@app.route('/headlines')
def headlines():
    with open('headlines.json') as f:
        return jsonify(dict, status=200) 
    # "<a href=%s>file</a>" % url_for('static', filename='headlines.json')

if __name__ == '__main__':
    app.run(debug=True)