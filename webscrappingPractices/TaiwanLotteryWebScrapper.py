# Writing a webcrawler to get the lottery numbers from Taiwan Lottery announcement webpage ---> hope I get BIG MONEY WHOOOHOOOO lol
#It will need to be changed when I have the time cause the government changes the Webpage at times occasionally
import requests
from bs4 import BeautifulSoup

url = "http://www.taiwanlottery.com.tw/"
html = requests.get(url)
html.encoding = "utf-8"

bs = BeautifulSoup(html.text, "html.parser")

data1 = bs.select("#rightdown")

data2 = data1[0].find("div", {"class":"contents_box2"})

data3 = data2.find_all("div", {"class":"ball_tx"})

#printing out the lucky NUMBERSSS BOOYA!

print("Lottery Nubmber in selected order:", end = "		")
for n in range(0,6):
	print(data3[n].text, end = "	")

print("\nLarge to Small:", end=" 	 ")
for n in range(6,len(data3)):
	print(data3[n].text, end = "	")

#second section
redball = data2.find("div", {"class":"ball_red"})
print("\n Second Section: {}".format(redball.text))
