from mechanize import Browser
from bs4 import BeautifulSoup as BS
import html5lib
from sys import argv
from random import randint
file1 = open(str(argv[1])+".txt","a",encoding="utf-8")
while(True):
    try:
        i = randint(100000,999999)
        br = Browser()
        br.set_handle_robots(False)
        br.set_handle_referer(False)
        br.set_handle_refresh(False)
        br.addheaders = [('User-agent', 'Firefox')]
        br.open('http://nhentai.net/g/'+str(i))
        soup = BS(br.response(),"html5lib")
        title = soup.find_all('span', class_="pretty")[0]
        title = str(title)[21:-7]
        print("\n")
        print(title)
        file1.write("\n"+title+"  #  nhentai.net/g/"+str(i))
    except Exception as err:
        print("erro:" + str(err))
file1.close()