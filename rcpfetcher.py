#Pull headline, title, author, date for each headline in https://www.realclearpolitics.com/2019/11/11/ and append to a list.

import json
import requests
import time
from bs4 import BeautifulSoup

url = 'https://www.realclearpolitics.com/2019/11/11/'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
headers = {'User-Agent': user_agent}

response = requests.get(url, headers=headers)
html_file = response.text

rcp_final_list = []

def print_headlines(html):
        soup = BeautifulSoup(html, 'lxml')
        title_tags = soup.find_all(attrs={"class": "title"})
        all_link_tags = []
        for tag in title_tags:
            links = tag.find_all('a')
            all_link_tags.append(links)
        return all_links
        
all_links = print_headlines(html_file)
for link in all links:
    print(link)