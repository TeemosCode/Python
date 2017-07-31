# -*- coding=utf-8 -*-

"""
Practing Requests module using request.get() to simulate HTTP GET method for sending out requests to server across the internet
it will send back a response ---> which is the HTML code. Access the codes using the "text" attribute
"""

import requests
url = "http://taqm.epa.gov.tw:80/pm25/tw/PM25A.aspx?area=1"

html = requests.get(url) # getting the html from the url with requests.get(url)
html.encoding = 'utf-8' #setting the encoding attribute of html
# get the text of the codes using html.text
print('=====the HTML code=====')
print(html.text) # the HTML CODE of the page of the url, exactly what we see in the browser

print('=====the END of HTML code=====')
print('--------------  -------------  -------------')
#getting the HTML code one line at a time
htmllist = html.text.splitlines()
for row in htmllist:
	print(row)

print('===============Finding appearance numbers of certain string===============')
#Looking for the appearances of a certain string in the HTML code(or the web page lol), the normal way
searchstr = input("What word to search in this webpage?:\n---> ")
count = 0
for row in htmllist:
	if searchstr in row:
		count += 1
print("Found string {}, {} times!".format(searchstr, count))
print('======================')
print("#next 'regexPractice.py' practices with using the 're' module, using regular expression to find certain patterns of strings in on the webpage")

