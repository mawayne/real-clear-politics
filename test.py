import requests
import json

source_url = 'http://127.0.0.1:5000/static/headlines.json'
source_response = requests.get(source_url)
source_content = source_response.text
source_content_list = json.loads(source_content)

print(source_content_list[1]['Title'])