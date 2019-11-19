# # Objective: Pull link, title, date, author, publication for each headline in https://www.realclearpolitics.com/2019/11/11/ and append to a list.

# Import requirements
import json
import requests
from bs4 import BeautifulSoup

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

# Create empty data list
rcp_final_list = []

# # Fetch links
# def get_url_link_tags(html):
#         soup = BeautifulSoup(html, 'lxml')
#         title_tags = soup.find_all(attrs={"class": "title"})
#         url_link_tags = []
#         for tag in title_tags:
#             link_tag = tag.find_all('a')
#             url_link_tags.extend(link_tag)
#         return url_link_tags
        
# url_link_tags = get_url_link_tags(html_file)
# all_url_links = []
# for link in url_link_tags:
#     link = link.attrs['href']
#     all_url_links.append(link)

# for url_link in all_url_links:
#     print(url_link)

# # Fetch titles
# url_link_tags = get_url_link_tags(html_file)
# all_titles = []
# for title in url_link_tags:
#     title = title.getText()
#     all_titles.append(title)

# for title in all_titles:
#     print(title)

# # Fetch authors
# def get_author_link_tags(html):
#         soup = BeautifulSoup(html, 'lxml')
#         byline_tags = soup.find_all(attrs={"class": "byline"})
#         author_link_tags = []
#         for tag in byline_tags:
#             link_tag = tag.find_all('a')
#             author_link_tags.extend(link_tag)
#         return author_link_tags

# author_link_tags = get_author_link_tags(html_file)
# all_authors = []
# for author in author_link_tags:
#     author = author.getText()
#     all_authors.append(author)

# for author in all_authors:
#     print(author)

# # Fetch sources
# soup = BeautifulSoup(html_file, 'lxml')
# source_tags = soup.find_all(attrs={"class": "source"})
# all_sources = []
# for source in source_tags:
#     source = source.getText()
#     all_sources.append(source)

# for source in all_sources:
#     print(source)

# Combine into one program

soup = BeautifulSoup(html, 'lxml')
post_tags = soup.find_all(attrs={"class": "post"})

headlines = []
for post in post_tags:
        title_class = post.find(attrs={"class": "title"})
        byline_class = post.find(attrs={"class": "byline"})
        if byline_class == None:
                continue
        source_class = post.find(attrs={"class": "source"})
        url_link_tag = title_class.find('a')
        author_link_tag = byline_class.find('a')
        link = url_link_tag.attrs['href']
        title = url_link_tag.getText()
        author = author_link_tag.getText()
        source = source_class.getText()
        headlines.append({'url': link, 'title': title, 'author': author, 'source': source, 'date': date})

for headline in headlines:
    print(headline['title'])


