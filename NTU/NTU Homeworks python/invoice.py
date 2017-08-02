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


    def handle_starttag(self , tag , attrs):
		if tag == 'span' and attrs == [('class' , 't18Red')]:
			self.action = 1


    def handle_data( self , data):
		if self.action == 1:
			self.invoice.append(data)
			
                
                        

    def hnadle_endtag(self , tag , attrs):
		pass


ans = invoiceparse()
ans.feed(content)
print(ans.invoice)
