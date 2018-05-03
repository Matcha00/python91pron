import requests
import re
import random
import time
from bs4 import BeautifulSoup
from proxy import getiplist








class download(object):

    def __init__(self):
        self.iplist = getiplist()
        # UA = random.choice(self.user_agent_list)
        # headers = {
        #     'User-Agent': UA,
        #     "Accept-Language": "zh-CN,zh;q=0.9",
        #     'X-Forwarded-For': self.randomIP,
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        #     'Accept-Encoding': 'gzip, deflate',
        #     'Referer': 'http://ip.zdaye.com/dayProxy.html',
        #     'Host': 'ip.zdaye.com',
        #     'Cookie': 'acw_tc=AQAAAEiBqm2vIAQALmyii8HMxtEmq5zb; ASPSESSIONIDSCAQADRD=EGIPCBKBMBCPKNGABPEBBGBD; ASPSESSIONIDQADSBDRD=OAHFDIKBFLKCHGMOFKDMGHCL; AJSTAT_ok_pages=7; AJSTAT_ok_times=1; __tins__16949115=%7B%22sid%22%3A%201513839668108%2C%20%22vd%22%3A%206%2C%20%22expires%22%3A%201513841503573%7D; __51cke__=; __51laig__=7; Hm_lvt_8fd158bb3e69c43ab5dd05882cf0b234=1513836125,1513839670,1513839695,1513839704; Hm_lpvt_8fd158bb3e69c43ab5dd05882cf0b234=1513839704',
        #     'Connection': 'keep-alive',
        #     'Upgrade-Insecure-Requests': '1'
        # }
        # html = requests.get("http://ip.zdaye.com/dayProxy/ip/12575.html", headers=headers)
        # html.encoding = 'gb2312'
        # pattern = re.compile(r'<b>.*?</b>')
        # iplisttn = BeautifulSoup(html.text, 'html.parser').find('div', class_='cont')
        # # print(iplisttn)
        # hhhh = re.findall(r'\d(.*?)@', iplisttn.text, re.S)
        # for ip in hhhh:
        #     ip_a = ip
        #     print(ip_a)
        #     self.iplist.append(ip_a)

        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

        self.ip_list = self.getiplist()
        self.randomIP = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(
            random.randint(0, 255)) + '.' + str(random.randint(0, 255))
        print('==================')
        #print(self.ip_list )



    def get(self,url,timeout, proxy=None,num_retries=6):

        UA = random.choice(self.user_agent_list)


        headers = {
            'User-Agent': UA,
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
            'X-Forwarded-For': self.ip_list[random.randint(1,50000)]
        }
        if proxy == None:
            try:
                 return  requests.get(url,headers = headers,timeout = timeout)
            except:
                if num_retries > 0:
                    time.sleep(10)
                    return self.get(url,timeout,num_retries-1)
                else:
                    time.sleep(10)
                    IP = ''.join(str(random.choice(self.iplist)))
                    proxy = {'http' : IP}
                    return self.get(url,timeout,proxy,)
        else:
            try:
                IP = ''.join(str(random.choice(self.iplist)))
                proxy = {'http': IP}
                return requests.get(url,headers = headers, proxies = proxy,timeout = timeout)
            except:

                if num_retries > 0:
                    time.sleep(10)
                    IP = ''.join(str(random.choice(self.iplist)))
                    proxy = {'http' : IP}
                    return self.get(url,timeout,proxy,num_retries - 1)
                else:
                    return self.get(url,3)

    def getiplist(self):
        iplist = []
        for i in range(50000):
            randomIP = str(random.randint(0, 255)) + '.' + str(random.randint(0, 255)) + '.' + str(
                random.randint(0, 255)) + '.' + str(random.randint(0, 255))
            iplist.append(randomIP)
            iplist = list(set(iplist))
        return iplist

    def getdown(self,url):

        UA = random.choice(self.user_agent_list)
        headers = {
            'User-Agent': UA,
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
            'X-Forwarded-For': self.randomIP
        }
        return requests.get(url, headers=headers)

request = download()


