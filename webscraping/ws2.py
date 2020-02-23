#SCRAPING IMDb

import requests
from requests_html import HTMLSession
import csv


session = HTMLSession()
file = open('imdb.csv','w')
writer = csv.writer(file)


head=['Title','Release Date','Rating','Poster']
writer.writerow(head)

r=session.get('https://www.imdb.com/chart/top/?sort=rk,asc&mode=simple&page=1')

list = r.html.find('.lister-list',first=True)

title = list.find('.titleColumn a')
release = list.find('.titleColumn span')
rating = list.find('.ratingColumn strong')
img = list.find('.posterColumn a img')


for i in range(len(rating)):
    r=[title[i].text,release[i].text,rating[i].text,img[i].attrs['src']]
    writer.writerow(r)




