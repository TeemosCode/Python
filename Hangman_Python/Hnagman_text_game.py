# -*- encoding = 'UTF-8' -*-
# getting rid of zip
# written by the coolest dude on earth: teemo!
# guess the words *****!
# gotten rid of all those swear words, was funny looking back though lmao XD
def match_up(inpt):
    a = '_' * len(inpt)
    print("Try guessing this word: " + a + "\n lET'S PLAY A GAME, u have 6 Chances yolo")
    l = list(a)
    words = []
    hp = 6
    lala = []
    while hp != 0:
        print('\nHP remaining:\n%d'% hp)
        if (''.join(l)) == server_input:
            restart= input("Yo ****!! You got it right! Congratulations! You survived for another day!!\nAnswer: %s\nWanna keep hanging?(Y/y):" % ("".join(l)) )
            restart = restart.lower()
#fixed --- 2017/7/31
            if restart == 'y':
                return True
            else:
                print("Good bye ****!!!")
                lala.append("FLAG")
                return False
            
            
        client_guess = input('Enter the character for guessing, choose carefully~! \n:')
        

        if len(client_guess) != 1:
            print("Please don't be blind, you can guess only ONE character !!!!\n What u have now:" , (''.join(l)) )


        elif client_guess not in server_input :
            if client_guess in words:
                print('Geeze~! I ALREADY told u u *****!! its not in the answer !\n What u have now:' , (''.join(l))  )
            else:
                words.append(client_guess)
                hp -= 1
                print('word NOT in answer! Lost 1 HP, you\'re dying~!\n What u have now:' , (''.join(l)) )
        elif client_guess in server_input:
            if client_guess in words:
                print('You\'ve already guessed this once, please guess another new one, don\'t wana get urself killed eh?!!\n What u have now:' , (''.join(l)) )
            else:
                print('\'%s\' in answer, NICE GUESS!!!'% client_guess)            
                words.append(client_guess)
                i = 0
                for c in server_input:
                    if c == client_guess:
                        l[i] = client_guess
                        i += 1
                        print('The answer now looks like this : \n%s' % (''.join(l)) )
                    else:
                        i+= 1
    if len(lala) > 0 :
        pass
    else:
        print('\nHP remaining:\n%d'% hp)
        print('*****! lost all the HP,u dead man. You got HANGED!')
        restart = input("Good Try though!\nWanna keep hanging?(Y/y):"  )
        restart.lower()
        if restart == 'y':
            match_up(server_input)
        else:
            print("Bye~")
            return False



if __name__ == '__main__':
    server_input = input('Enter a word for Guessing!\n:')
    while server_input != 'TeemoHasDied666':
        keepgoing = match_up(server_input)
        if not keepgoing:
            print("Bye~!!")
            break
        else:
            server_input = input('Enter a word for Guessing!\n:')
        
