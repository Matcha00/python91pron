import requests
from bs4 import BeautifulSoup
import os
import random
from download import request
from pymongo import MongoClient
from mogoqueue import MogoQueue
import threading
import multiprocessing

SLEEP_TIME = 1

class pron(object):


    def __init__(self):

        client = MongoClient()
        db = client['pron91']
        self.pron_collection = db['pron']
        self.title = ''
        self.url = ''
        self.show_url = ''






    def all_url(self, url):
        html = request.get(url,3)
        list_url = []
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_= "imagechannelhd").find_all('a')
        for a in all_a:
            href = a['href']
            list_url.append(href)
            print(href)
            self.url = href
            if self.pron_collection.find_one({'链接' : href}):
                print("kkkkk")
        else:
                self.movies(href)




    def movies(self,url_movies):
        movies_html = request.get(url_movies,3)
        movies_hrfe = BeautifulSoup(movies_html.text, 'lxml').find('div', class_="kk").find_all('a')
        for a in movies_hrfe:
            hhh = a['href']
            self.show_url = hhh
            post = { '链接' : self.url,
                     '详细链接' : self.show_url,
                     '标题' : self.title
                    }
            self.pron_collection.save(post)





    # def getPage(self,url):
    #     page = request.get(url,3)
    #     page_number = BeautifulSoup(page.text, 'lxml').find('div', class_= "pagingnav").find_all('a')
    #
    #     for a in page_number:
    #         page_last = a['title'][-1]
    #         return page_last + 1


    # def getdownload_url(self,strat,end):
    #     one_page = []
    #     for i in range(strat,end):
    #         page_url =  "http://91porn.com/video.php?category=rf&page=" + i
    #         one_page.append(page_url)









# Pron = pron()
#
# all_page =  Pron.getPage('http://91porn.com/video.php?category=rf')
# down_page = []
# start_page = input("输入开始页码")
# end_page = input("输入结束页码")
# if start_page > 0 & end_page < all_page & start_page < all_page:
#    down_page = Pron.getdownload_url(start_page,end_page)
# else:
#     print("页码超出范围")
#
# for aa in  down_page:
#  Pron.all_url(aa)