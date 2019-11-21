from flask import Flask
from flask import url_for

app = Flask(__name__, static_url_path='/Users/matthewwayne/dev/rcpolitics/static')


@app.route('/')
def home():
    return ('Hello, Biatch!')

@app.route('/send')
def send():
    return "<a href=%s>file</a>" % url_for('static', filename='headlines.json')

if __name__ == '__main__':
    app.run()