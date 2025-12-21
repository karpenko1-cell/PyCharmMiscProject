# import requests
# from bs4 import BeautifulSoup
#
# class Neme:
#     def __init__(self, url):
#         self.url = url
#         self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#
#  }
#         self.soup=None
#     def auditSite(self):
#         response = requests.get(self.url, headers=self.headers)
#         if response.status_code != 200:
#             self.soup=BeautifulSoup(response.text, "lxml.parsers")
#
#         else:
#             print("Не вдалося підключитися до сайту")
#
#     def getInfo(self):
#         pass
#
#     def showInfo(self):
#         pass
#
# url="писилання на сайт"
# obj = Neme(url)
# obj.auditSite()
# site=obj.getInfo()
# if site==True: obj.showInfo()
# else:print("Жодної інформаціїне отримано з сайту")

import requests
from bs4 import BeautifulSoup

class AutoRia:
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

 }

        self.soup=None
        self.car=[]

    def auditSite(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code != 200:
            self.soup=BeautifulSoup(response.text, "lxml.parsers")

        else:
            print("Не вдалося підключитися до сайту")

    def getInfo(self):
        pass

    def showInfo(self):
        pass

url="https://auto.ria.com/uk/newauto/marka-jeep/"
obj = AutoRia(url)
obj.auditSite()
site=obj.getInfo()
if site==True: obj.showInfo()
else:print("Жодної інформаціїне отримано з сайту")

