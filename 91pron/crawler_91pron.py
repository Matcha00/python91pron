import os
import time
import threading
import multiprocessing
from download import request
from mogoqueue import MogoQueue
from bs4 import BeautifulSoup
from pymongo import MongoClient, errors
SLEEP_TIME = 1


def crawler_91pron(max_threads=10):
    print('--------')
    crawl_queue = MogoQueue('pron91','hhh')

    def pageurl_crawler():
        while True:
             try:
                 url = crawl_queue.pop()
                 print(url)
             except:
                 print('no')
                 break


             else:

                 req = request.get(url,3)
                 req.encoding = 'utf-8'
                 title =  crawl_queue.pop_title(url)
                 all_show_url = BeautifulSoup(req.text, 'lxml').find('div', class_='videoplayer').find('source').get('src')
                 spider_show = MogoQueue('pron91','hhhh')
                 spider_show.push_show(all_show_url,title)
                 crawl_queue.complete(url)

    pageurl_crawler()

def process_crawler():
     process = []

     num_cpus = multiprocessing.cpu_count()
     for i in range(num_cpus):
         p = multiprocessing.Process(target=crawler_91pron)
         p.start()
         process.append(p)
         for p in  process:
             p.join()


if __name__ == "__main__":
    process_crawler()


# OUTSTANDING = 1
# PROCESSING = 2
# COMPLETE = 3
# db = 'pron91'
# collection = 'hhh'
# client = MongoClient(host='localhost', port=27017)
# Client = client[db]
# db = Client[collection]
# record = db.find_one()
# print(record)







