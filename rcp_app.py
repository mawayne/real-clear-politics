from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_url_path='/headlines' )

@app.route('/')
def home():
    return ('Hello, Biatch!')

@app.route('/headlines/<path:headlines.json>')
def send_headlines(path):
       headlines = send_from_directory('/rcpolitics', 'headlines.json', as_attachment = True)
       return jsonify([headline for headline in headlines])

if __name__ == '__main__':
       app.run(debug=True)