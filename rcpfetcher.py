# # Objective: Pull link, title, date, author, publication for each headline in https://www.realclearpolitics.com/2019/11/11/ and append to a list.

# Import requirements
import json
import requests
from bs4 import BeautifulSoup
import datetime
from datetime import timedelta, date
import time 

# Create necessary functions
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

def build_headline(post, dt):
    title_class = post.find(attrs={"class": "title"})
    byline_class = post.find(attrs={"class": "byline"})
    if byline_class == None:
        return
    source_class = post.find(attrs={"class": "source"})
    if source_class == None:
        return
    url_link_tag = title_class.find('a')
    author_link_tag = byline_class.find('a')
    if author_link_tag == None:
        return
    link = url_link_tag.attrs['href']
    title = url_link_tag.getText()
    author = author_link_tag.getText()
    source = source_class.getText()
    headline = {'url': link, 'title': title, 'author': author, 'source': source, 'date': dt}
    return headline
    

def get_headlines():
    # Create base_url variable
    base_url = 'https://www.realclearpolitics.com'
    # Create date range
    start_dt = date(2019, 9, 24)
    end_dt = date.today()
    # Start fetching headlines for each date in date range
    headlines = []
    for dt in daterange(start_dt, end_dt):
        dt = dt.strftime("%Y/%m/%d")
        # Prerequisites for server request
        url = base_url + '/' + dt + '/'
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
        headers = {'User-Agent': user_agent}
        # Attach time.sleep to server response
        time.sleep(1)
        response = requests.get(url, headers=headers)
        html = response.text
        # Extract post tags
        soup = BeautifulSoup(html, 'lxml')
        post_tags = soup.find_all(attrs={"class": "post"})
        # Extract headline data
        for post in post_tags:
            headline = build_headline(post, dt)
            headlines.append(headline)
    return headlines


if __name__ == '__main__':
    # Extract targeted info
    headlines = get_headlines()
    
    data_file = 'headlines.json'

    with open(data_file, 'w') as f:
        json.dump(headlines, f)

    with open(data_file, 'r') as f:
        headlines = json.load(f)

    for headline in headlines:
        clinton_mentions = 0
        if headline is None:
            continue
        if 'Clinton' in headline['title'] == True:
            clinton_mentions = clinton_mentions + 1
        elif 'Clintons' in headline['title'] == True:
            clinton_mentions = clinton_mentions + 1
        elif headline['title'] == None:
            continue
        else:
            clinton_mentions = 0
    print(clinton_mentions)
