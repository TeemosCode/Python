from bokeh.plotting import show, figure
from bs4 import BeautifulSoup as bs
import requests


url = "http://www.daxi-hro.tycg.gov.tw/home.jsp?id=25&parentpath=0,21,22"
content = requests.get(url).text
parse = bs(content, "html.parser")

person = []
year = []

data = parse.find("tbody")
rows = data.find_all("tr")

for row in rows[7:]:
	cols = row.find_all("td")
	if(len(cols) > 0):
		year.append(cols[0].text[:-1])
		person.append(cols[1].text)

f = figure(width = 800, height = 600, title = "Tao Yaun City Population History")
f.title_text_font_size = "20pt"
f.xaxis.axis_label = "Year"
f.yaxis.axis_label = "People"
f.line(year, person, line_width=3)
show(f)