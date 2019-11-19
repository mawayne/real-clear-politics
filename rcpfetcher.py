# # Objective: Pull link, title, date, author, publication for each headline in https://www.realclearpolitics.com/2019/11/11/ and append to a list.

# Import requirements
import json
import requests
from bs4 import BeautifulSoup


def build_headline(post_tag):
    title_class = post.find(attrs={"class": "title"})
    byline_class = post.find(attrs={"class": "byline"})
    if byline_class == None:
            return
    source_class = post.find(attrs={"class": "source"})
    url_link_tag = title_class.find('a')
    author_link_tag = byline_class.find('a')
    link = url_link_tag.attrs['href']
    title = url_link_tag.getText()
    author = author_link_tag.getText()
    source = source_class.getText()
    headline = {'url': link, 'title': title, 'author': author, 'source': source, 'date': date}
    return headline
    

if __name__ == '__main__':

    # Create base_url variable
    base_url = 'https://www.realclearpolitics.com'

    # Create date variable
    date = '2019/11/11'

    # Produce HTML file
    url = base_url + '/' + date + '/'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    headers = {'User-Agent': user_agent}

    response = requests.get(url, headers=headers)
    html = response.text

    soup = BeautifulSoup(html, 'lxml')
    post_tags = soup.find_all(attrs={"class": "post"})

    headlines = []
    for post in post_tags:
            headline = build_headline(post)
            headlines.append(headline)

    for headline in headlines:
        if headline is None:
            continue
        print(headline['title'])


