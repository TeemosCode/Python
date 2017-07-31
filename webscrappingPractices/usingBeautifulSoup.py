# -*- coding = "utf-8" -*-
# # practing BeautifulSoup for a better web scrapping experience and techniques to find more complex stuff
# practice using the Taiwan Lottery website
import requests
from bs4 import BeautifulSoup
#BeautifulSoup usage: BeautifulSoup(HTML Code, 'html.parser')
url = 'http://www.taiwanlottery.com.tw/'
html = requests.get(url)
bs = BeautifulSoup(html.text, 'html.parser')
print("---BeautifulSoup Attributes---")
print("title = {}\n---".format(bs.title))
print("text = {}\n---".format(bs.text))
print("find('tagstr') (finds the tag) = {}\n---".format(bs.find('a')))
print("find_all('tagstr') (finds ALL tags ---> as a LIST data structure) = {}\n---".format(bs.find_all("a")) )
print("select('CSS identifiers')  = {}\n---".format(bs.select("#id")))
#its a huge string of mess LOL!!!
print("""
	====================
	=                  =
	=                  =
	=                  =
	=    ==      ==    =
	=                  =
	=     ==    ==     =
	=      |====|      =
	=====================
	""")
print("the BeautifulSoup's select() method and its magic ---> used for finding certain ids and classes (usually the good things are in here on the web, wink* wink*)")
print("# select() return a LIST!")
data1 = bs.select("title")
print("title = {}".format(data1))
data1 = bs.select("#rightdown")
print("#rightdown = {}".format(data1))
data1 = bs.select(".title")
print(".title = {}".format(data1))

print("'html head title' = {}".format(bs.select("html head title")))
# de best stuff with find_all("tagstr", {"identifier":"itsvalue"})

print(bs.find_all("a", {"class":"sister"}))
print(bs.find_all("a", {"id":"link2"}))
#print("or")
#data3 = bs.select("#link2")
#print(data3[0].text)

#to find more than one tags, give the find_all([,,,,]) a list
print(bs.find_all(["a","title"]))
print("=======use get(attributestr) to get attribute content!!!")
data = bs.find("a")
print(data.get("href")) #http://fnc.ebc.net.tw/TaiwanLottery/
print()