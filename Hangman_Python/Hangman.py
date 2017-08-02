#Hangman GUI game

from tkinter import *

def ex():
    quit()

    

#sw = Frame.winfo_screenwidth()
#sh = Frame.parent.winfo_screenheigt()

#sx = (sw - 1000)/2
#sy = (sh - 700)/2

window = Tk()
window.title("Hangman Game")
window.geometry("1000x700")#???
#window.wm_iconbitmap('hangmanicon1.ico')

frame = Frame(window)
frame.pack()

canvas = Canvas(frame, width= 400, height = 400 , borderwidth = 1,relief = RAISED)
canvas.pack(pady = 20)
#the hanging machine (will be printed out once game starts)
canvas.create_line(200,25,350,25)
canvas.create_line(200,25,200,50)
canvas.create_line(350,25,350,375)
canvas.create_line(25,375,375,375)



#the label where answer displays, needs to be 'interactive' , might have to be created AFTER the game starts
answer = Label(window , bd = 4 , padx = 2, relief = RAISED , height = 3)
answer.pack()


#frame where buttons go
button_frame = Frame(window , relief = RAISED , bg = 'WHITE' )
button_frame.pack( side = BOTTOM , fill = Y)



#try placing buttons in the canvas (size)
bc = Canvas(button_frame , width = 600 , height = 300 , borderwidth = 1 , relief = RAISED)
bc.pack(pady = 20)


buttons = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
varRow = 0
varColumn = 0
columnspan = 1
for button in buttons:    
    command = lambda x=button: click(x)
    b = Button(bc , text = button , width = 4 , bg = 'gray' , fg = 'black'
               , padx = 4 , pady = 4 , command = command)
    b.grid(padx = 2 , pady = 2 , ipadx = 4, ipady = 4 , row = varRow , column = varColumn, columnspan = columnspan)
    varColumn += 1
    
    if varColumn > 8:
        varRow += 1
        varColumn = 0
    if varColumn == 8 and varRow == 1:
        columnspan = 2

#bodyparts displaying events when players get the wrong answers 
canvas.create_oval(155,50,245,140)#head
canvas.create_line(200,140,200,275)#body
canvas.create_line(200,167,137,230)#left arm
canvas.create_line(200,167,263,230)#right arm
canvas.create_line(200,275,137,338)#left leg
canvas.create_line(200,275,263,338)#right leg

 

def click(value):
    pass
    
    
    
    
#texting
#ext = Button(bc, text = 'Exit' , command = ex)
#ext.grid(padx = 20 , pady = 20)







window.mainloop()
