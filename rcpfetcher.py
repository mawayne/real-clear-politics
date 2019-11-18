#Pull link, title, author, date for each headline in https://www.realclearpolitics.com/2019/11/11/ and append to a list.

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

def get_all_link_tags(html):
        soup = BeautifulSoup(html, 'lxml')
        title_tags = soup.find_all(attrs={"class": "title"})
        all_link_tags = []
        for tag in title_tags:
            link_tag = tag.find_all('a')
            all_link_tags.extend(link_tag)
        return all_link_tags
        
all_link_tags = get_all_link_tags(html_file)
all_links = []
for link in all_link_tags:
    link = link.attrs['href']
    all_links.append(link)

print(all_links)    




