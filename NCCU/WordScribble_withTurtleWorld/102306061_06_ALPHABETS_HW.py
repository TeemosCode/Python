from swampy.TurtleWorld import *
from math import *
world = TurtleWorld()

bob = Turtle()
bob.delay = 0.0001


def poly_line(t,n,length,angle):
    for i in range(n):
        fd(t,length)
        lt(t,angle)


def arcr(t,r,angle):
    arc_length = 2*pi*r*angle/360
    n = int(arc_length/3) + 1
    step_length = arc_length/n
    step_angle = float(angle) / n
    lt(t,step_angle/2)
    poly_line_r(t,n,step_length,step_angle)
    rt(t,step_angle/2)

    
def poly_line_r(t,n,length,angle):
    for i in range(n):
        fd(t,length)
        rt(t,angle)


def movehv(t,length,angle1,angle2):
    """moves the turle horizontally
       without leaving a trail
       facing facing right
    """
    #or
    """
    moves turtle vertically 
    without leaving a trail
    facing upwards
    """
    lt(t,angle1)
    pu(t)
    fd(t,length)
    pd(t)
    rt(t,angle2)

def moverd(t,length,angle):
    """
    move diagonally right sidedly
    """
    pu(t)
    rt(t,angle)
    fd(t,length)
    lt(t,angle)
    pd(t)
    
def moveld(t,length,angle):
    """
    move diagonally left sidedly
    """
    pu(t)
    lt(t,angle)
    fd(t,length)
    rt(t,angle)
    pd(t)
    
def diagonally(t,angle,length,lt = lt):
    """Draws diaognally (whether it top to right bottom,
    or left to topright) decided by turning left oor right
    at what given angle end with facing right horizontally"""
    lt(t,angle)
    fd(t,length)
    rt(t,angle)

def diag(t,angle,length,lt = lt):
    lt(t,angle)
    fd(t,length)
    
def turnfb(t,length,angle,lt = lt):
    lt(t,angle)
    fdbk(t,length)

def fdbk(t,length):
    #goes forwards and back with just one f call
    fd(t,length)
    bk(t,length)
def arc(t,r,angle):
    arc_length = 2*pi*r*angle/360
    n = int(arc_length/3) + 1
    step_length = arc_length/n
    step_angle = float(angle) / n
    lt(t,step_angle/2)
    poly_line(t,n,step_length,step_angle)
    rt(t,step_angle/2)

# the alphabet functions
def a(t):
    diagonally(t,70,50,lt)
    diagonally(t,70,50,rt) 
    rt(t,40)
    moverd(t,25,70)
    fd(t,20)
    moveld(t,25,70)
    movehv(t,60,180,0)
#a(bob)

def b(t):
    arc(t,12.5,180)
    lt(t,180)
    arc(t,12.5,180)
    lt(t,90)
    fd(t,50)
    movehv(t,35,90,0)
    
#b(bob)

def c_(t):
    fd(t,30)
    bk(t,30)
    lt(t,90)
    fd(t,50)
    rt(t,90)
    fd(t,30)
    bk(t,30)
    rt(t,90)
    fd(t,50)
    lt(t,90)
    movehv(t,50,0,0)
    
#c_(bob)



def d(t):
    arc(t,25,180)
    lt(t,90)
    fd(t,50)
    lt(t,90)
    movehv(t,50,0,0)
#d(bob)


def e(t):
    def el(t):
        fd(t,35)
        bk(t,35)
        lt(t,90)
    def er(t):
        fd(t,25)
        rt(t,90)
    el(t)
    er(t)
    el(t)
    er(t)
    el(t)
    rt(t,180)
    fd(t,50)
    lt(t,90)
    fd(t,35)
    movehv(t,25,0,0)
#e(bob)

def f(t):
    lt(t)
    fd(t,25)
    rt(t)
    fdbk(t,20)
    lt(t)
    fd(t,25)
    rt(t)
    fd(t,20)
    movehv(t,50,270,270)
    movehv(t,20,0,0)
#f(bob)

def g(t):
    c_(t)
    movehv(t,15,180,90)
    fd(t,25)
    lt(t)
    fd(t,20)
    movehv(t,40,180,0)
    movehv(t,25,270,270)
#g(bob)

def h(t):
    lt(t)
    fd(t,25)
    fdbk(t,25)
    rt(t)
    fd(t,20)
    lt(t)
    fd(t,25)
    lt(t,180)
    fd(t,50)
    lt(t,90)
    movehv(t,30,0,0)
#h(bob)


def i(t):
    fd(t,35)
    bk(t,17.5)
    lt(t,90)
    fd(t,50)
    rt(t)
    fd(t,17.5)
    bk(t,35)
    movehv(t,50,270,0)
    movehv(t,70,90,0)
#i(bob)

def j(t):
    lt(t)
    fdbk(t,20)
    rt(t)
    fd(t,25)
    lt(t)
    fd(t,50)
    lt(t)
    fd(t,25)
    bk(t,40)
    movehv(t,50,90,270)
    movehv(t,20,0,0)
#j(bob)

def k(t):
    lt(t)
    fd(t,25)
    fdbk(t,25)
    rt(t,30)
    fdbk(t,30)
    rt(t,120)
    fd(t,30)
    movehv(t,25,60,0)
#k(bob)


def l(t):
    fdbk(t,35)
    lt(t,90)
    fdbk(t,50)
    movehv(t,55,270,0)
#l(bob)

def m(t):
    for i in range(2):
        diag(t,70,46,lt)
        diag(t,140,46,rt)
        lt(t,70)
    movehv(t,20,0,0)
#m(bob)

def n(t):
    lt(t)
    fd(t,50)
    diagonally(t,160,52,rt)
    lt(t,320)
    fdbk(t,50)
    rt(t,90)
    movehv(t,10,0,0)

#n(bob)
    
def o(t):
    movehv(t,10,0,0)
    arc(t,22,360)
    movehv(t,40,0,0)

#o(bob)

def p(t):
    lt(t)
    fd(t,20)
    rt(t)
    arc(t,15,180)
    lt(t)
    fd(t,50)
    movehv(t,40,90,0)
#p(bob)

def q(t):
    movehv(t,20,0,0)
    arc(t,25,360)
    movehv(t,25,90,135)
    fd(t,25*sqrt(2))
    movehv(t,25,45,0)
#q(bob)

def r(t):
    p(t)
    movehv(t,40,180,90)
    fd(t,20)
    rt(t,135)
    fd(t,20*sqrt(2))
    movehv(t,20,45,0)

#r(bob)

def s_(t):
    fd(t,15)
    arc(t,12,180)
    def poly_line_r(t,n,length,angle):
        for i in range(n):
            fd(t,length)
            rt(t,angle)

    def arcr(t,r,angle):
        arc_length = 2*pi*r*angle/360
        n = int(arc_length/3) + 1
        step_length = arc_length/n
        step_angle = float(angle) / n
        lt(t,step_angle/2)
        poly_line_r(t,n,step_length,step_angle)
        rt(t,step_angle/2)

    arcr(t,12,180)
    fd(t,15)
    movehv(t,48,270,0)
    movehv(t,30,90,0)
#s_(bob)

def t(t):
    lt(t)
    fd(t,50)
    lt(t)
    fd(t,20)
    rt(t,180)
    fd(t,40)
    movehv(t,10,0,0)
    movehv(t,50,270,270)
#t(bob)

def u(t):
    turnfb(t,50,90,lt)
    rt(t,90)
    fd(t,35)
    turnfb(t,50,90,lt)
    movehv(t,25,270,0)
#u(bob)

def v(t):
    movehv(t,50,90,150)
    fd(t,2*50/sqrt(3))
    lt(t,120)
    fd(t,2*50/sqrt(3))
    movehv(t,50,210,270)
    movehv(t,25,0,0)
#v(bob)

#movehv(bob,70,270,270)
#movehv(bob,1000,180,180)

def w(t):
    v(t)
    movehv(t,25,180,180)
    v(t)
#w(bob)
    
def x(t):
    lt(t,45)
    fd(t,50/sqrt(2))
    fdbk(t,50/sqrt(2))
    rt(t)
    bk(t,50/sqrt(2))
    fd(t,2*50/sqrt(2))
    movehv(t,25,45,0)
#x(bob)

def y(t):
    movehv(t,10,0,0)
    lt(t)
    fd(t,30)
    lt(t,30)
    fdbk(t,40/sqrt(3))
    rt(t,60)
    fdbk(t,40/sqrt(3))
    movehv(t,30,210,0)
    movehv(t,35,90,0)
#y(bob)

def z(t):
    fdbk(t,50)
    lt(t,45)
    fd(t,2*50/sqrt(2))
    lt(t,135)
    fdbk(t,50)
    movehv(t,50,90,0)
    movehv(t,25,90,0)
#z(bob)
    
    

if __name__ == "__main__":
    print'If You Want to see ALL alphabets-----(just type \'a\'~\'z\'later and you\'ll see)'
    print'-------------------------------'
    
    print 'Answer to Homework \'NCCU LAND ECONOMICS\''
    #movehv(bob,180,180,180)
    #movehv(bob,70,270,270)
    #movehv(bob,500,180,180)
    words = "nccu land economics"
    answer = {"n":n,"c":c_,"u":u,"l":l,"a":a,"d":d,"e":e,"o":o,"m":m,"i":i,"s":s_}
    
    ct = 0
    #answer = "nccu land economics"
    for c in words:
        ct +=1
        if c == 'o':
            movehv(bob,20,0,0)
            answer[c](bob)
        elif c == " " and ct == 5:
            movehv(bob,70,270,270)
            movehv(bob,190,180,180)
        elif c == " " and ct != 1:
            movehv(bob,25,0,0)
        else:
            answer[c](bob)
    
    movehv(bob,70,270,270)
    movehv(bob,750,180,180)
    
    s = raw_input( 'Want to try "MY" little game ?(Y[YES]/N[NO]): ' )
    s = s.upper()
    lib = {"a":a,"b":b,"c":c_,"d":d,"e":e,"f":f,"g":g,"h":h,"i":i,"j":j,"k":k,"l":l,"m":m,"n":n,"o":o,"p":p,"q":q,"r":r,"t":t,"s":s_,
           "u":u,"v":v,"w":w,"x":x,"y":y,"z":z}
    
    while s == 'Y' or s == 'YES':
        z = raw_input('What do u want to print out in ENGLISH?\n(If you do NOT type in english it WONT print a thing!): ')
        z = z.lower()
        cnt = 0
        for char in z:
            cnt+=1
            if char == " ":
                movehv(bob,50,0,0) # make a space between 'words' lolz
            elif char not in lib:
                print 'NOPE! It ISN\'T an Alphabet!(prints a lota times cause of its ENCODING)'
            else:
                lib[char](bob)


        ans = raw_input('Do u want to keep on playing?(Y/N): ')
        ans = ans.upper()
        if ans == 'Y' or ans == 'YES':
            movehv(bob,70,270,270) #move downwards to next line
            movehv(bob,cnt*50,180,180) # move back to where the turtle should initially be that would look better hehe
        else:
            break
    print 'End of Homework, have a nice day~~'
    print 'Now you can zoom round the turtle world too look at the words yo!!'

    wait_for_user()
    
