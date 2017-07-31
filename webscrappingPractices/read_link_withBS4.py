# a little cover up general practice with bs4
from bs4 import BeautifulSoup
import requests

url = "http://fnc.ebc.net.tw/TaiwanLottery/"
html = requests.get(url) # same thing as always, use the requests.get(url) or the url HTML webpage code
html.encoding = "utf-8" # same IMPORTANT thing!

bs = BeautifulSoup(html.text, "html.parser")
links = bs.find_all(["a", "img", "title"])

for link in links:
	href = link.get("href") # using the find_all . get("tagstr") method to find the tag attributes value and whats inside it hehe
	if href != None and href.startswith("http://"):
		print(href)
