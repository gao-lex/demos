import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from time import time
from threading import Thread
# 设置mongo
client = MongoClient('localhost', 27017)
db = client.DoubanMovie 
posts = db.th

start =time()
def Analysis_and_storage (url):
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

threads = []
for page in list(x*25 for x in range(0,10)):
    urls = 'https://movie.douban.com/top250?start='+str(page)+'&filter='
    t = Thread(target=Analysis_and_storage, args=(urls,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time()
print ('Cost {} seconds'.format((end - start)))