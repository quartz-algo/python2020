#SCRAPING IMDb - Coming Soon Page

import requests
from requests_html import HTMLSession
import csv


session = HTMLSession()
'''
file = open('comingsoon.csv','w')
writer = csv.writer(file)


head=['Title',]
writer.writerow(head)
'''

r=session.get('https://www.imdb.com/movies-coming-soon/?ref_=nv_mv_cs')

list = r.html.find('.list',first=True)

item = list.find('.list_item',first=True)

title = item.find('h4 a',first=True)
#print(title.text)
time = item.find('time',first=True)
#print(time.text)
genre = item.find('span')
#for g in genre:
#    print(g.text,end='\t')
#print()
desc = item.find('.outline',first=True)
#print(desc.text)
cast = item.find('.txt-block')
#for c in cast:
#    print(c.text)
img = item.find('.image a div img',first=True)
#print(img.attrs['src'])
