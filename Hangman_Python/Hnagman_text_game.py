#encoding = 'UTF-8'
# getting rid of zip
#written by the coolest dude on earth: teemo!
#guess the words fuckass!

def match_up(inpt):
    a = '_' * len(inpt)
    print("Try guessing this u fuckboy!!: " + a + "\n lET'S PLAY A GAME, u have 6 Chances yolo")
    l = list(a)
    words = []
    hp = 6
    lala = []
    while hp != 0:
        print('\nHP remaining:\n%d'% hp)
        if (''.join(l)) == server_input:
            restart= input("Yo fuckboy!! Your little shithead got it right!\nAnswer: %s\nWanna keep hanging?(Y/y):" % ("".join(l)) )
            restart = restart.lower()
#fixed --- 2017/7/31
            if restart == 'y':
                return True
            else:
                print("Good bye FUCKBOY!!!")
                lala.append("shithole")
                return False
            
            
        client_guess = input('Guess the words fuckass!\n:')
        

        if len(client_guess) != 1:
            print("fuck u mother~~~ guess only ONE character u dumbass!!!!\n What u have now:" , (''.join(l)) )


        elif client_guess not in server_input :
            if client_guess in words:
                print('You mother fucker!! I ALREADY told u u fuckass! its not in the fucking answer dick!\n What u have now:' , (''.join(l))  )
            else:
                words.append(client_guess)
                hp -= 1
                print('word not in answer ,fuckass lost 1 HP, you suck!\n What u have now:' , (''.join(l)) )
        elif client_guess in server_input:
            if client_guess in words:
                print('You\'ve already guessed this once u fuckboy!!\n What u have now:' , (''.join(l)) )
            else:
                print('\'%s\' in answer, dayum shit luck fuckass!!'% client_guess)            
                words.append(client_guess)
                i = 0
                for c in server_input:
                    if c == client_guess:
                        l[i] = client_guess
                        i += 1
                        print('the answer now looks like this fuckass:\n%s' % (''.join(l)) )
                    else:
                        i+= 1
    if len(lala) > 0 :
        pass
    else:
        print('\nHP remaining:\n%d'% hp)
        print('fuckass lost all the HP,u dead man, man u suck!')
        restart = input("Yo fuckboy!! Your little shithead crave for another HOLE!\nWanna keep hanging?(Y/y):"  )
        restart.lower()
        if restart == 'y':
            match_up(server_input)
        else:
            print("Bye~")
            return False



if __name__ == '__main__':
    server_input = input('let thoses asses guess a word yo!')
    while server_input != 'fuck':
        keepgoing = match_up(server_input)
        if not keepgoing:
            print("Bye~!!")
            break
        else:
            server_input = input('let thoses asses guess a word yo!')
        

