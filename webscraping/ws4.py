#SCRAPING ANOTHER TEST WEBSITE USING BeautifulSoup
from bs4 import BeautifulSoup
import requests
import csv

f = open('book.csv','w')
fw = csv.writer(f)

head =['NAME','PRICE','IMAGE']
fw.writerow(head)

for i in range(1,51):
    url = f'http://books.toscrape.com/catalogue/page-{i}.html'
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')
    #print(soup.prettify())
    bk = soup.find_all('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

    for b in bk:
        name = b.h3.a.attrs['title']
        price = b.find('div',class_='product_price').p.text[1:]
        img_src = b.div.a.img.attrs['src']
        img_url = f'http://books.toscrape.com/{img_src}'

        #r = [name,price,img_url]
        fw.writerow([name,price,img_url])
        #print(name)
        #print(price)
        #print(img_url)
        #print()
f.close()