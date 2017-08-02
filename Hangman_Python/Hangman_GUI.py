#testing, developing area

#v1.7
from tkinter import *
import random

root = Tk()
##
root.state('zoomed')
##
root.title("Hangman")
root.geometry("1000x700")
root.wm_iconbitmap('hangmanicon1.ico')

#datas of answers for users to guess



guess_words = {
  
'Animals': 
'zebra,monkey,dog,cat,fish,vulture,bird,weasel,whippet,wolf,wolverine,wombat,woodpecker,\
swan,sparrow,sponge,snake,snail,seal,shark,saola,scorpion,rat,rabbit,moth,poodle,pid,\
piranha,pika,peacock,parrot,hedgehog,hyena,falcon,eagle,echidna,elephant,emu,cuscus,crocodile,booby,\
bobcat,bloodhound,chinook,dragonfly,dolphin,donkey,dachshund,dalmatian,capybara,barnacle,abyssinian,ant,avocet,axolotl', 

'Food':
'Acorn,almond,anchovy,anise,appetizer,appetite,apple,apricot,Artichoke,asparagus,aspic,avocado,Blackberry\
,bland,blueberry,Boysenberry,bran,bread,breadfruit,breakfast,brisket,broccoli,broil,Brownie,brunch,buckwheat\
,buns,burrito,bacon,bagel,bake,banana,basil,Batter,beancurd,beans,beef,beet,berry,biscuit,bitter,cake,\
calorie,candy,cantaloupe,capers,caramel,carbohydrate,carrot,cashew,cassava,casserole,cater,cauliflower,Caviar,celery,cereal,\
chard,cheddar,cheese,cheesecake,chef,cherry,chew,chicken,chili,Chips,chives,chocolate,chopsticks,chow,chutney,cilantro,cinnamon,\
citron,citrus,clam,cloves,cobbler,coconut,Cod,coffee,cookie,corn,cornflakes,cornmeal,crab,crackers,cranberry,Cream,crepe,crisp,crunch,\
crust,cucumber,cupcake,curds,currants,curry,custard,dessert,dough,doughnut,dragonfruit,Dressing,durian,Egg,Eggplant,fish,flour,frosting,\
fruit,garlic,ginger,gingerale,gingerbread,grain,grape,grapefruit,gravy' , 

'Everday Life':
'school,bus,toilet,piss,poop,kitchen,room,bedroom,television,tv,television,wifi,internet,car,bicycle,pillow,blanket,sheet,clothes,wardrobe,\
bed,table,study,class,teacher,classmates,lights,buttons,cellphones,phone,watch,sex,porn,masturbation,hospital,eat,lunch,\
breakfast,toothbrush,mirror,stairs,sun,talking,walking,shitting,computer,internet,wifi,gaming,waiting,idling,thinking,sleep,\
sleeping,eating,nap,napping,drinking,exercise,money,job,work,working,sex,sex,music,dancing,money,coin,creditcard,shopping,shop,mrt,bus',     

'Movies':
'Avatar,Lincoln,Turbo,The Avengers,Twilight,Ghandi,Savages,Descent,Gravity,Inception,ant man,inside out,meet the fockers,the intern,the hunger games\
Up,rain man,the martian,fast and furious,avengers,the incredible hulk,the intern,Jump,Godzilla,King Kong,Exodus,Inception,Interstellar,Iron man,pan,spider man,bat man,cat girl,the edge of tomorrow,star wars\
Gravity,Stella,Pinocchio,Labrynth,Hook,Arachnophobia,Cinderella,E T,lord of the rings,saving private ryan,jaws,\
treasure island,frozen,salt,fury,maleficent,lucy,noah,Hercules,Pompeii,wolves,blackhat,the godfather,gone with the wind,wizard of Oz,Elysium,\
men in black,steve jobs,concussion,',

'Games':
'diablo,starcraft,warcraft,monopoly,diablo,starcraft,monopoly,world of warcraft,starcraft,sim,simcity,monopoly,\
revelation,everquest,diablo,starcraft,warcraft,sim,simcity,league of legends,dota,infamous,fallout,fragile,monopoly,titan,ogre,ra,samurai,rage,\
shogun,uno,bang,battleships,worms,tetris,zoom,abducted,abyss,azzl,tetris battle,league of legends,dynasty warriors,need for speed,battlefield the sims,\
command and conquer,mass effect,need for speed,gundam,age of empires,clash of clans'


}

#================================important GLOBAL variables=============================================
#Answer, it will be changed by the call() function to the current answer in user choosen genre
answer = ''
    #answer to list (to b displayed)
a = ("_" + " ")*len(answer)
#MAIN checking reference , the LIST to '.join()' back to the way it is and display it
check = list(a)
#reference to HP, to know what bodyparts to hang
hp = 6

#================================important GLOBAL variables=============================================


topFrame = Frame(root)
topFrame.pack( )

topLFrame = Frame(topFrame)
topLFrame.pack(side = LEFT)

#dictionary keys for guesses, buttons come out after START button is pressed,START button itself disappears
#START button command
def appear():
    guess = ['Animals','Food','Everday Life','Movies','Games']
    vrow = 0
    vcolumn = 0

    for button in guess:
        
        command = lambda x=button: call(x)#calling words for guessing
        
        if button == 'Animals':
            background = 'brown'
            foreground = 'white'
        elif button == 'Food':
            background = 'coral'
            foreground = 'blue'
        elif button == 'Everday Life':
            background = 'khaki1'
            foreground = 'SystemHighlight'
        elif button == 'Movies':
            background = 'cyan'
            foreground = 'black'
        elif button == 'Games':
            background = 'LightSteelBlue1'
            foreground = 'tomato'
        b = Button(topLFrame , text = button , width = 10 , height = 3,
                   bg = background  , fg = foreground, command = command)
        b.grid(padx = 8 , pady = 2 , ipadx = 5, ipady = 2 ,
               row = vrow , column = vcolumn)

        vrow += 1

        if vcolumn > 1:
            vrow += 1
            vcolumn = 0
        
    endb = Button(topRFrame , text = 'QUIT' ,width = 10, height =3,bg = 'red' ,
                  fg = 'black', bd = 5 , relief = RAISED, command = hide)
    endb.grid(padx = 8, pady = 2 , ipadx = 5 , ipady = 2 , row = 3 , column = 2)
    hide_start_B()
    topl.config(text = 'Choose a Genre' , bg = 'burlywood1', fg = 'black' )#label changes  
    
    
#function for hiding START button
def hide_start_B():
    for button in topRFrame.grid_slaves():
        if int(button.grid_info()['row']) == 1:
            button.grid_forget()
    
#same as the QUIT button, pops out after START button clicked
#QUIT stops the current game, hides itslef and the other buttons in this function, wipes out the label answers,START button reappears
def hide_guess_B():
    for buttons in topLFrame.grid_slaves():
        buttons.grid_forget()
#hides the QUIT button
def hide_quit_B():
    for button in topRFrame.grid_slaves():
        if int(button.grid_info()['row']) == 3:
            button.grid_forget()

#creating START button
def startB(): 
    startb = Button(topRFrame, text = 'START' , width = 10 , height = 3, bg = 'gold' ,
                    fg = 'dark violet', bd = 5 , relief = RAISED, command = appear)
    startb.grid(padx = 8, pady = 2 , ipadx = 5 , ipady = 2 , row = 1 , column = 2)    
    
#QUIT button command, hides all other buttons and lines, reappear START button    
def hide():
    global hp
    hp = 6
    hide_guess_B()
    hide_quit_B()
    startB()#creates the START button
    topl.config(text = 'Click Start to Play' , bg = 'honeydew2' , fg = 'black')
    del_canvas_lines()
    topc.create_line(200,25,350,25)
    topc.create_line(200,25,200,50)
    topc.create_line(350,25,350,375)
    topc.create_line(25,375,375,375)
    delete_canvas()

    
#CALL the guessing word value for further useage, also creating the keyboard buttons for gaming purpose
#button commands for the 'KINDS'
def call(value):
    l = guess_words[value].split(',')
    n = random.randint(0,len(l) - 1)
    global answer
    answer = l[n].upper()
    
    
    if " " in answer:#########################
        label_show = ""
        for c in answer:
            if c != " ":
                label_show = label_show + "_" + " "
            elif c == " ":
                label_show = label_show + " " + " "#######################
    elif ' ' not in answer:
        label_show = ("_" + " ")*len(answer)
        
    global a
    a = label_show
    
    global check
    check = list(a) 
            #label changes to _ _ _ _ ... depending on the given answer , aslo changes its fg, bg color
            #according to different buttons
    topl.config(text = a)
    if value == 'Animals':
        topl.config(bg = 'brown' , fg = 'white')
    elif value == 'Food':
        topl.config(bg = 'coral' , fg = 'blue' )
    elif value == 'Everday Life':
        topl.config(bg = 'khaki1' , fg = 'SystemHighlight' )
    elif value == 'Movies':
        topl.config(bg = 'cyan' , fg = 'black' )
    elif value == 'Games':
        topl.config(bg = 'LightSteelBlue1' , fg = 'tomato' )      


    
    hide_guess_B()
    create_buttons()

        
#functions for deleting the hanged mans body parts
def del_canvas_lines():
    topc.delete(ALL)
    
'''    
def del_head():
    topc.delete(head)
def del_body():
    topc.delete(body)
def del_leftArm():
    topc.delete(leftA)
def del_rightArm():
    topc.delete(rightA)
def del_leftLeg():
    topc.delete(leftL)
def del_rightLeg():
    topc.delete(rightL)
'''

#deleting the keyboards(placed in the canvas)
def delete_canvas():
    for canvas in bottomFrame.pack_slaves():
        canvas.pack_forget()



topMFrame = Frame(topFrame)
topMFrame.pack(side = LEFT)

topRFrame = Frame(topFrame)
topRFrame.pack(side = LEFT)

bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM )

#CANVAS
topc = Canvas(topMFrame, width= 400, height = 400 , borderwidth = 1,
              relief = RAISED ,bg = 'AntiqueWhite1')
topc.pack(fill = BOTH)
topc.create_line(200,25,350,25)
topc.create_line(200,25,200,50)
topc.create_line(350,25,350,375)
topc.create_line(25,375,375,375)


#the LABEL
topl = Label(topMFrame , bd = 4 , padx = 2, relief = RAISED , height = 2 , pady = 2,
             text = 'Click Start to Play' , bg = 'honeydew2', font ='Helvetica 16 bold italic')
topl.pack(fill = BOTH)


#START game button, dissapears when clicked
startb = Button(topRFrame, text = 'START' , width = 10 , height = 3, bg = 'gold' ,
                fg = 'dark violet', bd = 5 , relief = RAISED, command = appear)
startb.grid(padx = 8, pady = 2 , ipadx = 5 , ipady = 2 , row = 1 , column = 2)

# creating a global object for canvas, so it could be invisible before getting created(======so it looks better XD======) 
botc = Canvas()

#creates canvas with keyboard buttons inside
def create_buttons():
    global botc # calling the global canvas to be changed ( so it can appear )
    botc = Canvas(bottomFrame , width = 600 , height = 300 , borderwidth = 1 , relief = RAISED ,
                  bg = 'honeydew2')
    botc.pack(fill = BOTH , pady = 50)

    buttons = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    varRow = 0
    varColumn = 0
    columnspan = 1
    for button in buttons:    
        command = lambda x=button , r = varRow , c = varColumn , cs = columnspan  : click(x , r , c , cs )
        b = Button(botc , text = button , width = 4 , bg = 'gray' , fg  = 'black'
                   , padx = 4 , pady = 4 , command = command)
        b.grid(padx = 2 , pady = 2 , ipadx = 4, ipady = 4 , row = varRow ,
               column = varColumn, columnspan = columnspan)
        varColumn += 1

        if varColumn == 10 and varRow ==0:
            varRow += 1
            varColumn = 0
            columnspan = 2
        if varColumn == 9 and varRow == 1:
            varRow += 1
            varColumn = 0
            columnspan = 4

    
    
def restartB():
    restartb = Button(topRFrame , text = 'RESTART' , width = 10 , height =3, bg = 'lawn green' 
                          , fg = 'black', bd = 5 , relief = RAISED, command = restart)
    restartb.grid(padx = 8, pady = 2 , ipadx = 5 , ipady = 2 , row = 3 , column = 2)

def delete_label():
    for label in topLFrame.pack_slaves():
        label.pack_forget()
    
    
def restart():
    global hp
    hp = 6
    del_canvas_lines()
    topc.create_line(200,25,350,25)
    topc.create_line(200,25,200,50)
    topc.create_line(350,25,350,375)
    topc.create_line(25,375,375,375)    
    delete_canvas()
    delete_label()    
    appear()
    
    
            
#BUTTONS clicked, main gaming function!!!!!!!!!!!!!!!!            
def click(value, row , column, columnspan): 
    global hp# the reference to the body parts
    global answer# the actual STRING answer
    global check# the list to be checked
    
    # disabling the buttons once clicked
    # =======================================NEED BETTER SOLUTION!!!!!!!!!====================================
    
    
    b = Button(botc , text = value , width = 4 , bg = 'black' , fg  = 'white'
                   , padx = 4 , pady = 4 , command = NONE , state = DISABLED)#disable buttons after being clicked
    b.grid(padx = 2 , pady = 2 , ipadx = 4, ipady = 4 , row = row , column = column ,
           columnspan = columnspan)
    
    
    # =======================================NEED BETTER SOLUTION!!!!!!!!!====================================
    
    if value in answer:
        i = 0
        for char in answer:
            if value == char:
                check[i*2] = value
                i += 1
            else:
                i += 1
        display = ''.join(check)
        topl.config(text = display)

        # FIXED THIS SHIT!!!! FUCKING HEADACHE ARGHHHHHHHHHHHHHHHHHHHHHHHH!!!!!!

        ans = ''.join(check).split(" ")
        counter = 0
        key = 0
        for n in range(len(ans)):
            if ans[n] == '':
                if ans[n - 1] == '':
                    ans[n] = ' '
            else:
                pass
                
       #############ARGH!!!!!!!!!!!!!!!!!!!!!!             
            ###GOT IT LOLZZZZZ MAN I SUCKKK
        a = ''.join(ans)
        
        if a == answer: #Player got it all RIGHT
            #creates a label telling the players they won!! will need to b deleted when RESTART button is clicked!!!
            endl = Label(topLFrame , bd = 4 , padx = 2, relief = RAISED , height = 2 ,
                         pady = 2, text = 'YOU WIN!', bg = "DarkGoldenrod1" , fg = 'red2' , font = "Times 15 bold ")
            print('\a')
            endl.pack()  
            hide_quit_B()#QUIT button disappears

            #creates restart button
            restartB()
            delete_canvas()
        #!!!!!!!!!!!!!!!!!!!

            
    else:
        # ==============AGAINST THE 'D R Y' RULES!!!!! FIGURE IT OUT!!!! HOW TO SIMPLIFY IT!!!!!====================
        hp -= 1
        if hp == 5:
            head = topc.create_oval(155,50,245,140)#head
        elif hp == 4:
            body = topc.create_line(200,140,200,275)#body
        elif hp == 3:
            leftA = topc.create_line(200,167,137,230)#left arm
        elif hp == 2:
            rightA = topc.create_line(200,167,263,230)#right arm
        elif hp == 1:
            leftL = topc.create_line(200,275,137,338)#left leg
        elif hp == 0:
            rightL = topc.create_line(200,275,263,338)#right leg
            
            hide_quit_B()#QUIT button disappears
            restartB()
            #creates a label telling the players they won!! will need to b deleted when RESTART button is clicked!!!
            endl = Label(topLFrame , bd = 4 , padx = 2, relief = RAISED , height = 3 
                         , pady = 2, text = 'You\'re HANGED!\nAnswer:\n%s' % answer ,
                         bg = 'OrangeRed2' , fg = 'magenta4' , font = 'Verdana 10 bold italic')
            endl.pack()  
            delete_canvas()
            
root.mainloop()
