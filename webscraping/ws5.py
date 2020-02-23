#SCRAPING ANOTHER TEST WEBSITE USING BeautifulSoup
from bs4 import BeautifulSoup
import requests
import csv

f = open('quote.csv','w')
fw = csv.writer(f)

h = ['QUOTE','AUTHOR','LINK','TAGS']
fw.writerow(h)

for i in range(1,11):
    url = f'http://quotes.toscrape.com/page/{i}/'
    src = requests.get(url).text
    soup = BeautifulSoup(src,'lxml')

    block = soup.find_all('div',class_='quote')

    for b in block:
        quote = b.span.text.replace(';','')
        print(quote)
        author = b.find('small',class_='author').text
        print(author)
        link = b.find('a').attrs['href']
        linkurl = f'http://quotes.toscrape.com/{link}'
        print(linkurl)
        try:
            tag = b.div.text
            print(tag)
        except:
            tag = 'NULL'
            print(tag)
        fw.writerow([quote,author,linkurl,tag])


f.close()