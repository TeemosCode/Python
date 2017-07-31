import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
import requests

# empty lists for data we grab from the government website later to append it in then use it to plot wheeeee
year = []
person = []

url = "http://www.daxi-hro.tycg.gov.tw/home.jsp?id=25&parentpath=0,21,22"
content = requests.get(url).text
parse = bs(content, "html.parser")
data = parse.find("tbody")
rows = data.find_all("tr")



for row in rows[7:]: # the government changed its layout, the front 6 rows contains nothing, so I start from the 7th row
	cols = row.find_all("td")
	if(len(cols) > 0):
		year.append(cols[0].text[:-1])
		person.append(cols[1].text)

plt.plot(year, person, linewidth="2.0")
plt.title("TaoYuan City Population History")
plt.xlabel("Year (R.O.C year)")
plt.ylabel("People")

plt.savefig("TaoYuan City Population History.jpg")#saving it whhhheeeeeee
plt.show()
