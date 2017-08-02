#encoding = 'utf-8'
#server
import socket
import sys
from _thread import *
import service

host = 'localhost'
port = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

    
s.listen(5)
print("waiting for user connection...")


def money(i):
        c = 0
        l = 0
        i = i[::-1]
        for n in service.headprize:
            if l < len(i):
                for ch in reversed(n):
                    if ch == i[l]:
                        c += 1
                        l+=1
                    else:
                        break
            else:
                pass
        conn.send(str.encode("對中了--!!'   %d   '!!--個號碼(從後面數來)\n "%c) )

def threaded_client(conn):
    initiate = 'The month of receipt:\n%s\n發票號碼： %s\n有錢領的末三碼： %s\n'%(service.ans.month_display[0], service.ans.invoice[0:4] , service.ans.match )
    conn.send(str.encode(initiate ))
    while True:
        try:
            data = conn.recv(1024)
            reply = data.decode('utf-8')
            if reply == service.grandprize[0][-3:] or reply == service.grandprize[1][-3:]:
                conn.send(str.encode("DINNNNNNNNNNNNNG~~!!!: 後三碼和特大獎的一樣喔!!!!") )
                data = conn.recv(1024)
                reply = data.decode('utf-8')
                if reply == service.grandprize[0][:3] or reply == service.grandprize[1][:3]:
                    string = "喔喔喔喔喔喔喔喔喔喔!!!!一樣喔~~~剩中間兩個職做確認!\n請看--->   %s" % (service.grandprize[0] + "     " + service.grandprize[1])
                    conn.send(str.encode( string ))
                else:
                    conn.send(str.encode("‧‧>_<‧‧哀哀哀哀~~~可惜啊!!!!千萬不是那麼好種的啊 哈哈哈!!!!!"))
    
            elif reply in service.ans.match:
                conn.send(str.encode("\n!!!!!!!!!!!!!!!!!!中獎囉!!!!!繼續對~~~~!!!!!!!!!!!!!!!!!!!\n來看看有沒有對到更多吧!!!"))
                data = conn.recv(1024)
                reply = data.decode('utf-8')
                money(reply)

            elif reply not in service.ans.match :        
                conn.send(str.encode('XXX可惜沒中XXX~~繼續加油XXX\n'))
        except:
            
            print('client:' + addr[0] + '對完了~~不玩了!!')
            conn.close()
            break
            
            

#starts main service
service.ans.print_number()
while True:
    conn , addr = s.accept()
    print('connected to : '+ addr[0] + ': '+str(addr[1]))
    start_new_thread(threaded_client, (conn,))
    
    
