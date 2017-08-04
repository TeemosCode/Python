# -*- coding: utf-8 -*-
#102306061 資管三甲  何秉哲
from math import *


def B_height(x1,y1,x2,y2,HA,i,t,degree):
    def distance(x1,y1,x2,y2):
        distant = sqrt( (x1-x2)**2 + (y1-y2)**2 )
        print 'Distant between the two points with coordinates ( %.5f , %.5f )\
 and ( %.5f , %.5f ) = %.5f \n' % (x1,y1,x2,y2,distant)
        return distant
    distant = distance(x1,y1,x2,y2)
    V = distant * tan(degree*pi/180)
    hAB = V + i/100.0 - t
    B_height = HA + hAB
    print 'Height of B = %.5f' % B_height
    return B_height


def check_user_input(s, input_value):
    ti = 0
    try:
        i = float(input_value)
    except Exception as e:
        print 'BUG --> ' , e
        print'please retry '
        ti = 1
    while ti == 1:
        i = raw_input(s)
        ti = 0
        try:
            i = float(i)
        except Exception as e:
            print 'BUG --> ' , e
            print' please retry '
            ti = 1
    return i

B_height(3,4,9,12,23.158,150,2,30)


while True:
    s = raw_input("Want to check it out yourself? (Y[YES]) : ")
    s = s.upper()
    if s == 'Y' or s == 'YES':
        s = 'Enter x1 coordinate: '
        x1 = raw_input(s)
        x1 = check_user_input(s,x1)
        s = 'Enter y1 coordinate: '
        y1 = raw_input(s)
        y1 = check_user_input(s,y1)
        s = 'Enter x2 coordinate: '
        x2 = raw_input(s)
        x2 = check_user_input(s,x2)
        s = 'Enter y2 coordinate: '
        y2 = raw_input(s)
        y2 = check_user_input(s,y2)
        s = 'Enter A\'s Height: '
        HA = raw_input(s)
        HA = check_user_input(s,HA)
        s = 'Enter Intrument(儀器高) Height: '
        i = raw_input(s)
        i = check_user_input(s,i)
        s = 'Enter Height of t(覘標高): '
        t = raw_input(s)
        t = check_user_input(s,t)
        
        s = 'Enter degrees: '
        degree = raw_input(s)
        degree = check_user_input(s,degree)
        print 'Here\'s your Answer' ,B_height(x1,y1,x2,y2,HA,i,t,degree) 
    else:
        print 'Good bye! Have a nice day~~'
        break


