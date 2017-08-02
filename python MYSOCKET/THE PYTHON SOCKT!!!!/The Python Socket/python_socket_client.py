#encoding = 'UTF-8'
#socket client
import socket, sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = 'localhost'
port = 5555

s.connect((host,port))

print('Connected to :'+ host + '  via  port :' + str(port) )

print(s.recv(1024).decode('utf-8'))

while True:
    i = input("-------輸入發票末三碼-------\n(如果沒發票對了請輸入('N'))\n--->")
    i = i.upper()
    if i == 'N':
        s.close()
        break
    s.send(str.encode(i))
    data = s.recv(1024).decode('utf-8')
    print(data)
    if data == "DINNNNNNNNNNNNNG~~!!!: 後三碼和特大獎的一樣喔!!!!" :
        print(data)
        c = input("---輸入前三碼看看吧!!!~~希望能重千萬!!!---\n:")
        s.send(str.encode(c))
        data = s.recv(1024).decode('utf-8')
        if "喔喔喔喔喔喔喔喔喔喔!!!!一樣喔~~~剩中間兩個職做確認!" in data:
            print(data)

        else:
            print(data)

    elif data == "\n!!!!!!!!!!!!!!!!!!中獎囉!!!!!繼續對~~~~!!!!!!!!!!!!!!!!!!!\n來看看有沒有對到更多吧!!!":
        print(data)
        c = input("請輸入所有的發票號碼吧\n--->")
        while len(c) != 8:
            c = input("輸入的位數跟發票不符合(為8位數)，請重新輸入!： \n--->")
        s.send(str.encode(c))
        data = s.recv(1024).decode('utf-8')
        print(data)
            

    elif data == 'XXX可惜沒中XXX~~繼續加油XXX\n':
        print(data)
    
