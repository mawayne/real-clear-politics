from flask import Flask, jsonify, json, request
import json

app = Flask(__name__)

data_file = 'headlines.json'
with open(data_file) as f:
    headlines = json.load(f)

headlines_author = []
headlines_date = []
headlines_source = []
headlines_title = []
headlines_url = []

@app.route('/')
def home():
    return ('Hello, Biatch!')

@app.route('/headlines/all', methods=['GET'])
def send_headlines_all():
    return jsonify(headlines) 

@app.route('/headlines', methods=['GET'])
def headlines_sources():
    # if 'author' in request.args:
    #     headlines_author = request.args['title']
    
    # if 'date' in request.args:
    #     headlines_date = request.args['title']

    if 'source' in request.args:
        headlines_source = request.args['source']
    
    if 'title' in request.args:
        headlines_title = request.args['title']

    # if 'url' in request.args:
    #     headlines_url = request.args['title']
    
    source_results = []

    # for headline in headlines:
        # if headlines_source in headline['source']:
        #     source_results.append(headline)    
    # return jsonify(source_results)

    for headline in headlines:
        # if headlines_source in headline['source']:
        #     source_results.append(headline)
        if headlines_title in headline['title']:
            source_results.append(headline) 
    return jsonify(source_results)

if __name__ == '__main__':
    app.run(debug=True)