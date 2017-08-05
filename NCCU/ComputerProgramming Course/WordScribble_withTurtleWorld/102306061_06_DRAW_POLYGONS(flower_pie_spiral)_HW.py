#-*- encoding:utf-8 -*-
#102306061 資管三甲 何秉哲 HW_
#Drawings of PIE, FLOWER and SRPIRAL
from swampy.TurtleWorld import *
from math import *
import random

world = TurtleWorld()

bob = Turtle()
bob.delay = 0.001

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

def move(t,length):
    pu(t)
    fd(t,length)
    pd(t)


def poly_line(t,n,length,angle):
    for i in range(n):
        fd(t,length)
        lt(t,angle)

#function for drawing pies
def draw_pies(t,n):
    vertex = 360.0/n #等邊三角形之頂角角度
    sides = 50 #訂死三角型之邊常
    side = sqrt( 2*sides**2*(1-cos(vertex*pi/180)) ) #以餘弦定理算出多角形之邊常
    triangle_side_angel=(180-vertex)/2 #等邊三角形底角
    big_turn = triangle_side_angel + vertex #要轉的大角度(烏龜劃的時候)
    for i in range(n):
        lt(t,big_turn)
        fd(t,side)
        lt(t,big_turn)
        fd(t,sides)
        lt(t,180)
        fd(t,sides)

"""
draw_pies(bob,10)
draw_pies(bob, 5)
"""

def arc(t,r,angle):
    arc_length = 2*pi*r*angle/360
    n = int(arc_length/3) + 1
    step_length = arc_length/n
    step_angle = float(angle) / n
    lt(t,step_angle/2)
    poly_line(t,n,step_length,step_angle)
    rt(t,step_angle/2)
    

def draw_spiral(t, n=500, length=3, a=0.1, b=0.0002):
    """Draws an Archimedian spiral starting at the origin.
    我太弱了!!!想不到SPIRAL之數學公式，所以先用作業的解答看看
    Args:
      n: how many line segments to draw
      length: how long each segment is
      a: how loose the initial spiral starts out (larger is looser)
      b: how loosly coiled the spiral is (larger is looser)

    http://en.wikipedia.org/wiki/Spiral
    """
    theta = 0.0

    for i in range(n):
        fd(t, length)
        dtheta = 1 / (a + b * theta)
###########################################################??????
        lt(t, dtheta)
        theta += dtheta

#draw_spiral(bob,20)
    
#arc(bob,60)
def draw_petal(t,r,angle):
    for i in range(2):
        arc(t,r,angle)
        lt(t,180-angle)
        
def draw_flowers(t,n,r=50,angle=60):
    for i in range(n):
        draw_petal(t,r,angle)
        lt(t,360.0/n)


#draw_flowers(bob, 10 ,50 , 60)
if __name__ == '__main__':
    print 'Drawing the requirements of the Homework'
    print'-------------------------------------------'
    print'Drawing 8 slices of Pie-----'
    draw_pies(bob,8)
    movehv(bob,60,0,0)
    #movehv(bob,70,270,270)
    print 'Drawing 8 petals of Flower-----'
    draw_flowers(bob,8,r=50,angle=60)
    movehv(bob,150,0,0)
    
    
    print'Drawing a 500 twirl of Spiral-----'
    draw_spiral(bob, n=500, length=3, a=0.1, b=0.0002)
    movehv(bob,300,5,0)
    #movehv(bob,70,270,270)
    movehv(bob,70,270,270)
    movehv(bob,600,180,180)
    l = [1,2,3]
    while True:
        a = raw_input('What would you like me to draw?\n(choose [1] for "flowers",\
[2] for "Pies"  [3] for "spiral"): ')
        ti = 0
        try:
            a = int(a)
        except ValueError:
            print 'You CAN\'T type in anything other than the integers of those choices yo!'
            ti = 1
        while ti == 1:
            a = raw_input('What would you like me to draw?\n(choose [1] for "flowers",\
[2] for "Pies"  [3] for "spiral"): ')
            ti = 0
            try:
                a = int(a)
            except ValueError:
                print 'You CAN\'T type in anything other than the integers of those choices yo!'
                ti = 1
        if a not in l:
            print 'Since you can\'t understand that there are only three choices, guess i\'ll choose for you!'
            a = random.randint(1,3)
        if a == 1:
            print 'chose to draw a FLOWER'
            n = raw_input('How many petals of a flower do you want?(remember to input numbers!!): ')
            try:
                n = int(n)
            except ValueError:
                print 'You CAN\'T type in anything other than the integers yo!!!'
                ti = 1
            while ti == 1:
                ti = 0
                n = raw_input('How many petals of a flower do you want?(remember to input numbers!!): ')
                try:
                    n = int(n)
                except ValueError:
                    print 'You CAN\'T type in anything other than the integers yo!!!'
                    ti = 1
            
            draw_flowers(bob,n,r=50,angle=60)
            movehv(bob,60,0,0)
        if a ==2:
            print 'Chose to draw a PIE'
            n = raw_input("How many slices of pie do you want? (numbers only!!)")
            try:
                n = int(n)
            except ValueError:
                print'You CAN\'T type in anything other than the integers yo!!!'
                ti = 1
            while ti == 1:
                ti = 0
                n = raw_input("How many slices of pie do you want? (numbers only!!)")
                try:
                    n = int(n)
                except ValueError:
                    print'You CAN\'T type in anything other than the integers yo!!!'
                    ti = 1
            print'Drawing %d slices of pie~~~' % n
            draw_pies(bob,n)
            movehv(bob,60,0,0)
        if a == 3:
            print 'Chose to draw a spiral'
            n = raw_input("How many twirls of spiral do you want? (numbers only!![suggest over 500 to see the MAGIC]!!)")
            try:
                n = int(n)
            except ValueError:
                print'You CAN\'T type in anything other than the integers yo!!!'
                ti = 1
            while ti == 1:
                ti = 0
                n = raw_input("How many twirls of spiral do you want? (numbers only!![suggest over 500 to see the MAGIC]!!)")
                try:
                    n = int(n)
                except ValueError:
                    print'You CAN\'T type in anything other than the integers yo!!!'
                    ti = 1
            print'Drawing %d twirls of spiral~~~' % n
            draw_spiral(bob, n, length=3, a=0.1, b=0.0002)
            movehv(bob,60,0,0)
            
        z = raw_input("Still want to play?(Y/N)")
        z = z.upper()
        if z == 'Y':
            pass
        else:
            print'Good Bye, Have a nice day~~~!!!'
            print ' You can zoom around to look at what the turtle world looks like now weepeeee!!!!'
            break
    wait_for_user()
