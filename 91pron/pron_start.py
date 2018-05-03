from download import request
from mogoqueue import MogoQueue
from bs4 import BeautifulSoup

spider_queue = MogoQueue('pron91','crwal_queue')


def getPage(url):
    page = request.getdown(url)
    page_number = BeautifulSoup(page.text, 'lxml').find('div', class_= "pagingnav").find_all('a')
    print(page_number[-2].string)
    return int(page_number[-2].string) + 1


def getdownload_url(strat,end):
    one_page = []
    for i in range(strat,end+1):
        aaaaaa = "http://91.91p23.space/v.php?category=tf&viewtype=basic&page=" + str(i)
        one_page.append(aaaaaa)
    return one_page
    print(one_page)


           # page_url =  "http://91.91p23.space/video.php?category=rf" + str(++i)
           # return one_page.append(page_url)
           # print(one_page)

def start(url):
    html = request.getdown(url)
    html.encoding = 'utf-8'
    all_a = BeautifulSoup(html.text, 'lxml').find('div', id= "videobox").find_all(class_='listchannel')
    for a in all_a:
        a_url = a.find('a').get('href')
        image_title = a.find('a').find('img').get('title')
        print('正在存入数据')
        spider_queue.push(a_url,image_title)

if __name__ == "__main__":
    all_page =  getPage('http://91.91p23.space/v.php?category=tf&viewtype=basic&page=1')
    down_page = []
    start_page = int(input("输入开始页码"))
    end_page = int(input("输入结束页码"))
    #if start_page > 0 & end_page < all_page & start_page < all_page:
    down_page = getdownload_url(start_page,end_page)
    print(down_page)
    #else:
        #print("页码超出范围")

    for aa in  down_page:
        start(aa)
