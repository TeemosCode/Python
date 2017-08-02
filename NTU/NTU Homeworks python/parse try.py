import urllib.request
from html.parser import HTMLParser

web = urllib.request.urlopen('https://tw.movies.yahoo.com/movieinfo_main.html/id=5794')
webcon = web.read().decode('utf_8')
web.close()

class MYHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.action = 0
        self.action2 = 0
        
    def handle_starttag(self , tag , attrs):
        if tag == 'span' and attrs == [('class' , 'tit')]:
            self.action = 1
        elif tag == 'span' and attrs == [('class' , 'dta')]:
            self.action2 = 1
        elif tag == 'div' and attrs ==[('class') , ('text full')]:
            pass
            


    def handle_data(self , data):
        if self.action == 1:
            print(data , end = ' ')
            self.action = 0
        elif self.action2 == 1:
            print(data, end = '\n')
            self.action2 = 0
        elif data == '劇情簡介':
            print(data , end =': ')
            
    def handle_endtag(self , tag):
        pass


Parse = MYHTMLParser()
Parse.feed(webcon)




    

