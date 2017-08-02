import urllib.request
from html.parser import HTMLParser
data = urllib.request.urlopen('http://invoice.etax.nat.gov.tw')
content = data.read().decode('utf_8')
data.close()

class invoiceparse(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.action = 0
        self.invoice = []
        self.month = 0
        self.month_display = []
    def handle_starttag(self , tag , attrs):
        if tag == 'span' and attrs == [('class' , 't18Red')] :
            self.action = 1
        elif tag == 'h2':
            self.month = 1
            
    def handle_data(self , data):
        if self.action == 1:
            self.invoice.append(data)
            self.action = 0
        elif self.month == 1 and  (b in data)  :
            self.month_display.append(data)
            self.month = 0
        
        
    
b = input("要對幾月份的發票? (輸入一個阿拉伯數字) :")
ans = invoiceparse()
ans.feed(content)
print(ans.month_display[0])
print(ans.invoice[0:4])


a = input('對發票囉!!')
