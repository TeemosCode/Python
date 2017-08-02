#encoding = 'utf-8'
#server
import socket
import sys
from _thread import *
import service

host = 'localhost'
port = 4444

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
    
    while True:
        print('Client deciding what to do...............')
        conn.send(str.encode('想做什麼?  (A) 對發票 (B) Play Text Style HangMan'))
        data = conn.recv(1024)#收到回答要做啥
        reply = data.decode('utf-8')
        if reply == 'A':
            print('-----Client 對發票中-----')
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

                    elif reply == 'N':
                        print('Client 不對了, Client has no more invoice left...(I guess)')
                        break
                    
                    elif reply not in service.ans.match :        
                        conn.send(str.encode('XXX可惜沒中XXX~~繼續加油XXX\n'))
                    
                except:
            
                    print('client:' + addr[0] + '對完了~~不玩了!!')
                    conn.close()
                    break
        elif reply == 'B':
            print('Client wants to play HangMan, Let\' Hang em!!')
            while True:
                ask = '\nLet\'s Play a Game!! Its called HangMan!!, Do you DARE venture into this world?(\'Y\'to keep playing \'N\' to RUN AWAY!!)'
                conn.send(str.encode(ask))
                data = conn.recv(1024)#接A or B
                reply = data.decode('utf-8')
                if reply == 'N':
                    print("Client 不玩了--- He's a little chicken, he ran........")
                    conn.send(str.encode('Bye you little CHICKEN!!'))
                    break
                elif reply == 'Y':
                    
                    guess = input("Word for the client to be hanged!!! :")
                    guess = guess.lower()
                    tp = input("Type of word for client reference :")
                    
                    words = []
                    hp = 7
                    lala = []

                    
                    a = ('_' + ' ') * len(guess)

                    l = list(a) 
                    lis = []
                    text = "\nGues this! Your life depends on it!: " + a + "\n LET'S PLAY THE GAME! You have 7 chances! The word is about\n" + tp + '  Guess 1 word at a time!!'
                    conn.send(str.encode(text))#送屁話啊
                    
                    #data = conn.recv(1024)#沒內容(不想打亂順序)
                    #reply = data.decode('utf-8')#沒內容(不想打亂順序)
                    while hp != 0:
                        hp_left = '\nChances remaining:\n%d'% hp
                        conn.send(str.encode(hp_left))#tell client chances left
                        print('\nClient has %d chances remaining'% hp)
                        
                        data = conn.recv(1024)
                        reply = data.decode('utf-8')#接到答案 == client 端的 guess
            
                        #開始判斷 
                        if reply not in guess :
                            #沒猜中任何字元 
                            if reply in words: #看低能有沒有重複猜到
                                wrong = '\nYou\'ve already guessed it before dumbass!!\nWhat u have now:' + (''.join(l))
                                conn.send(str.encode(wrong))
                            else:#沒重複猜到錯誤的
                                words.append(reply)
                                hp -= 1
                                if hp ==0:
                                    break
                                else:
                                    wrong = '\nWRONG!. You lost 1 chance, you suck!\nWhat u have now:' + (''.join(l))
                                    conn.send(str.encode(wrong))
                        elif reply in guess:
                            if reply in words:
                                wrong = '\nYou\'ve already guessed this once u dumbass!!\nWhat u have now:' + (''.join(l)) 
                                conn.send(str.encode(wrong))
                            else:
                                right_guess = '\n\'%s\' IN answer, still more to go!!'% reply
                                words.append(reply)
                                i = 0
                                for c in guess:
                                    if c == reply:
                                        l[i*2] = reply
                                        i += 1
                                        
                                    else:
                                        i+= 1

                                
                                        
                                if (''.join(''.join(l).split())) == guess:#see if client got dis right, if they servived or not lol and would they wanna continue
                                    print('Damn it!!! Client got it right, let\' try hanging them again!!')
                                    right = "Correct!!!! Wow, you got it RIGHT!\n Guess its time... FOR THE NEXT ONE HAHAHA!"
                                    conn.send(str.encode(right))#送結束屁話
                                    break #client贏了，跳出判斷迴圈

                                right_guess_reply = right_guess + 'the answer now looks like this fuckass:\n%s\n' % (''.join(l)) 
                                conn.send(str.encode(right_guess_reply))
                                
                    if hp == 0:
                        print('We HANGED the client. Client Hanged! Client dead! Waiting to see if client wants to revive and try again.......')
                        conn.send(str.encode('You lost all your chances!\n Chances: 0\nYou Are HANGED, Your DEAD!!!!'))#送結束屁話
                        
                                
                                
                                
#starts main service
service.ans.print_number()
while True:
    conn , addr = s.accept()
    print('connected to : '+ addr[0] + ': '+str(addr[1]))
    start_new_thread(threaded_client, (conn,))
    
    

