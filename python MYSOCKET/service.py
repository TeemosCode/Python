#service_module
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
        self.match = []
    def handle_starttag(self , tag , attrs):
        if tag == 'span' and attrs == [('class' , 't18Red')]:
            self.action = 1
        elif tag == 'h2':
            self.month = 1
            
    def handle_data(self , data):
        if self.action == 1:
            self.invoice.append(data)
            self.action = 0
        elif self.month == 1 and '年' in data:
            self.month_display.append(data)
            self.month = 0
    def print_number(self):
        for n in self.invoice[0:4]:
            if len(n) > 16:
                print(n[5:8] + '\n' + n[14:17] + '\n' + n[-3:])
                for i in n.split("、"):
                    self.match.append(i[-3:])
                #self.match = [n[5:8] , n[14:17] , n[-3:] ]
            elif 9 < len(n) < 16:
                for i in n.split('、'):
                    self.match.append(i)
                    print(i)


ans = invoiceparse()
ans.feed(content)
grandprize = ans.invoice[:2]
headprize = ans.invoice[2].split("、")

def money(i):
        c = 0
        l = 0
        i = i[::-1]
        if len(i) != len(headprize[0]):
            enter = input("輸入的位數跟發票不符合(為8位數)，請重新輸入!： \n--->")
            money(enter)
        else:
            for n in headprize:
                if l < len(i):
                    for ch in reversed(n):
                        if ch == i[l]:
                            c += 1
                            l+=1
                        else:
                           break
                else:
                    pass
        print("對中了--!!'   %d   '!!--個號碼(從後面數來)\n "%c)


#main function
def service():
    print('The month of receipt:\n%s'%ans.month_display[0])
    print(ans.invoice[0:4] , '\n')
    ans.print_number()
    print(ans.match)
    while True:
        a = input("-------輸入發票末三碼-------\n(如果沒發票對了請輸入('N'))\n--->")
        
        a = a.upper()
        
        if a == grandprize[0][-3:] or a == grandprize[1][-3:]:
            print("DINNNNNNNNNNNNNG~~!!!: 後三碼和特大獎的一樣喔!!!!")
            c = input("---輸入前三碼看看吧!!!~~希望能重千萬!!!---\n:")
            if c == grandprize[0][:3] or c == grandprize[1][:3]:
                
                print("喔喔喔喔喔喔喔喔喔喔!!!!一樣喔~~~剩中間兩個職做確認!")
                print("請看--->   ", end = "")
                print(grandprize[0] + "     " + grandprize[1] + "\n")
            else:
                print("‧‧>_<‧‧哀哀哀哀~~~可惜啊!!!!千萬不是那麼好種的啊 哈哈哈!!!!!\n")
        elif a in ans.match:
            print("\n!!!!!!!!!!!!!!!!!!中獎囉!!!!!繼續對~~~~!!!!!!!!!!!!!!!!!!!\n")
            print("來看看有沒有對到更多吧!!!")
            c = input("請輸入所有的發票號碼吧\n--->")
            money(c)
            
        elif a not in ans.match and a != 'N':
            print('XXX可惜沒中XXX~~繼續加油XXX\n')
        else:
            print("對完囉!!!!")
            break

if __name__ == '__main__':

    print(ans.match)
    service()

    
    
