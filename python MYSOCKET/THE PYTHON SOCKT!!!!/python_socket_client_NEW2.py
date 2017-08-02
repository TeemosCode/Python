#socket client
import socket, sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = 'localhost'
port = 4444

s.connect((host,port))

print('Connected to :'+ host + '  via  port :' + str(port) )

ls = ['A','B']
be_a_man = ['Y','N']
while True:
    data = s.recv(1024).decode('utf-8')#被問想做啥
    #if data == '想做什麼?  (A) 對發票 (B) Play Text Style HangMan':
    print(data)#問想做啥
    ans = input("所以呢?: ")
    ans = ans.upper()
    while ans not in ls:
        print("請選擇 (A) 或 (B)")
        print(data)#問想做啥
        ans = input("所以呢?: ")
        ans = ans.upper()
    s.send(str.encode(ans))#回答要做啥 (A) 或 (B)
    if ans == 'A':
        print(s.recv(1024).decode('utf-8'))
        while True:
            i = input("-------輸入發票末三碼-------\n(如果沒發票對了請輸入('N'))\n--->")
            i = i.upper()
            if i == 'N':
                s.send(str.encode(i))
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
    elif ans == 'B':
        while True:
            
            data = s.recv(1024).decode('utf-8')#asked to play hangman or not
            print(data)
            a = input('What would you do? Be a MAN(\'Y\')? Or run like the wind?(\'N\')')
            a = a.upper()
            while a not in be_a_man:
                print('Choose \'Y\' or \'N\'')
                a = input('What would you do? Be a MAN(\'Y\')? Or run like the wind?(\'N\')')
                a = a.upper()
            if a == 'N':
                s.send(str.encode(a))
                data = s.recv(1024).decode('utf-8')
                print(data)
                break
            elif a == 'Y':
                s.send(str.encode(a))#送y
                print('\n----- waiting for server to reply -----\n')
                data = s.recv(1024).decode('utf-8')#收到屁話
                print(data)#人家講屁話
                #s.send(str.encode(''))
                
                while True:
                    data = s.recv(1024).decode('utf-8')
                    print(data)#sever tells how much life left
                    answer = input('Let\'s do this!(Only ONE character at a time)\n:')
                    answer = answer.lower()
                    while len(answer) != 1:
                        print("都說只能一次打一個字了，你他媽英文怎能爛成這樣?!重打!!\nAlready told you to guess ONE character at a time dumbass!!Guess AGAIN!")
                        answer = input('Let\'s do this!(Only ONE character at a time)\n:')
                        answer = answer.lower()
                    s.send(str.encode(answer))#傳達案，SERVER開始判斷

                    data = s.recv(1024).decode('utf-8')#接到判斷後結果
                    print(data)
                    
                    #繼續輸入，server等待(while回圈內起始地方)
                    if data == "Correct!!!! Wow, you got it RIGHT!\n Guess its time... FOR THE NEXT ONE HAHAHA!":#代表贏了!!!
                        break
                        #看要不要重玩吧!
                    elif data =='You lost all your chances!\n Chances: 0\nYou Are HANGED, Your DEAD!!!!':#被ko之後的屁話
                        break
                        
                    else:
                        pass
                print('你復活囉，想開始重玩嗎?')
                    #看要不要重玩







