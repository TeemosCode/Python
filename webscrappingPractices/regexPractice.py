# -*- coding="utf-8" -*-

"""
# practing regular expression with the python "re" module to search for certain patterns of strings on webpages

# to check out regular expressions, go to ---> http://pythex.org/  to check it out!
"""

#examples of a few regex
# variable names: [A-Za-z_][A-Za-z0-9_]* (meaning can appear 0<= times <= INF)
#Email : [A-Za-z0-9_]+@[a-zA-Z0-9\._]+ (appearing 1<= times ,+ INF)
#Url : http://[A-Za-z0-9\./_]+

# using re.compile("regex"): to get the regular expression

import re
pattern = re.compile("[a-z]+")
matches = pattern.match("yologg887788onetwothree") # get the strings that match the regular expression in the string
#same as the below code, no need for using the compile() method
matches = re.match(r'[a-z]+', "yologg887788onetwothree")

print("=====Matching regular expression '[a-z]+' to 'yologg887788onetwothree' string using the match() method (returns strings that matches until it hits parts that don't match)=====")
print('The matches:')
print(matches) 
#the match() attributes
print("===The match() attributes===")

print("matches.group() = {}".format(matches.group())) 
print("matches.start() = {}".format(matches.start()))
print("matches.end() = {}".format(matches.end()))
print("matches.span() = {}".format(matches.span()))

print("========Using the Search() method=====")
print("The search() method returns the FIRST match it finds")
searches = re.search(r'[a-x]+' , "1234yolofuloyo!7788hohoho")
print("The searched matches:")
print(searches)
print("===== The search() attributes =====")

print("searches.group() = {}".format(searches.group()))
print("searches.start() = {}".format(searches.start()))
print("searches.end() = {}".format(searches.end()))
print("searches.span() = {}".format(searches.span()))

print("=====What the match() method will find=====")
matches = re.match(r'[a-x]+', "1234yolofuloyo!7788hohoho")
print(matches) # the matches can't find anything (cause the first thing it hits doesn't match --> so returns None)
"""print("matches.group() = {}".format(matches.group())) 
print("matches.start() = {}".format(matches.start()))
print("matches.end() = {}".format(matches.end()))
print("matches.span() = {}".format(matches.span()))
It'll find nothing, so None type has NO ATTRIBUTES"""
print("===================================")

print("----Using findall() method to return a LIST that encludes ALL string patterns found-----")
allMatches = re.findall(r'[a-x]+' , "1234yolofuloyo!7788hohoho")
print("what findall() finds: ")
print(allMatches)

print("Using regular expressions to find Emails on Taiwans 中華電信 (A ISP in Taiwan, huge company... worked with my professor and my team once, not very friendly to work with, expecially the $ grants lmao...)")

import requests, re
regex = re.compile("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+") # regex for Email patterns
url = 'https://auth.cht.com.tw/ldaps/'
html = requests.get(url)
emails = regex.findall(html.text) # mach the regular expression to the html.text in the webpage for the email patterns to find all the email strings
print('The Emails-->:')
for email in emails:
	print(email)