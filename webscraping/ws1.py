#SCRAPING A TEST WEBSITE

import requests
from requests_html import HTMLSession

session = HTMLSession()
r=session.get('http://172.16.104.50/')
code = r.html.find('h1',first=True)
article = r.html.find('h2')
#sum = r.html.find('p')

for i in article:
    print(article[i].text)