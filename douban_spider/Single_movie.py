import requests
from bs4 import BeautifulSoup
import pymongo
from pymongo import MongoClient
from time import time
client = MongoClient('localhost', 27017)
db = client.DoubanMovie 
collection = db.Single
posts = db.temp

for page in list(x*25 for x in range(0,10)):
    url = 'https://movie.douban.com/top250?start='+str(page)+'&filter='
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")
    for info in soup.find_all(class_='info'):
        name = info.find('a').text.strip('\n')
        introduction = info.find('p').text.strip()
        score = info.find(class_='rating_num').text
        try:
            inq = info.find(class_='inq').text
        except AttributeError:
            inq = ''
        post = {
            'name':name,
            'introduction':introduction,
            'score':score,
            'inq':inq,
        }
        posts.insert_one(post)
# Cost 4.598546266555786 seconds