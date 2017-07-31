# -*- coding = utf-8 -*-

"""
Practicing with the python urllib module for url handling and control
"""

from urllib.parse import urlparse
url = 'http://taqm.epa.gov.tw:80/pm25/tw/PM25A.aspx?area=1'

print('---------------------\nFecthing url of Taipei Government PM2.5 URL using urllib.parse to look at the url\n------------------')
urlpar = urlparse(url)
print('------------\nthe url ParseResult object...\n-----------')
print(urlpar)

print("=============\nbreaking it down: ParseResult attribute\n================")
print("scheme={}".format(urlpar.scheme))#http
print("netloc=%s" % urlpar.netloc) # tam.epa.gov.tw:80
print("port = {}".format(urlpar.port))# 80
print("path = %s" % urlpar.path) # /pm25/tw/PM25A.aspx
print("query= %s " % urlpar.query) # area = 1
print("fragment = {}".format(urlpar.fragment)) #empty string
print("params = {}".format(urlpar.params)) # empty string

