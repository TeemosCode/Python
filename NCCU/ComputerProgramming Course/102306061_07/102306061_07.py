#-*- coding: Big5 -*-
#第一大題
import random
from math import *
#1.
print "--------------------第一大題--------------------"
print '(         先自己寫死參數測試各個函數功能          ) '
def dd2dms(degrees):
    circumference = degrees // 360.0
    degree = (degrees % 360.0)
    a_degree = degree // 1  #我們要的degree表示法, 'a_' stands for answer
    minutes = ((degree % 1) * 60 )
    a_minutes = minutes // 1 #我們要的minutes表示法, 'a_' stands for answer
    a_seconds = (minutes%1) * 60 #我們要的second表示法, 'a_' stands for answer
    print ' %.3f Degrees = %d circumference, %d degree, %d minutes, %.3f seconds' %(degrees,circumference,a_degree,a_minutes,a_seconds)
    return circumference,a_degree, a_minutes , a_seconds


print '第一題 :'
dd2dms(325.136)

#2.
def dms2dd(circumference = 0, degree = 0 , minute = 0, second = 0):
    degrees = circumference * 360 + degree + minute/60.0 + second / 3600.0  #角度運算式
    print ' %d circumference, %d degree, %d minute, %f second = %.3f degrees' % (circumference , degree, minute, second, degrees)
    return degrees


print '第二題 :'
dms2dd(2,16,43,48)
    
    
#3.
def findXY(length,angle):
    angle_in_radians = angle * pi / 180
    quadrant = angle % 360.0 #看餘數判斷所在象限
    if quadrant <= 90: #在第一象限內
        coordinate_x = cos(angle_in_radians) * length
        coordinate_y = sin(angle_in_radians) * length
    elif quadrant > 90 and quadrant <= 180: #第二象限
        coordinate_x = -cos(angle_in_radians) * length
        coordinate_y = sin(angle_in_radians) * length
    elif quadrant > 180 and quadrant <= 270:  #第三象限
        coordinate_x = -cos(angle_in_radians) * length
        coordinate_y = -sin(angle_in_radians) * length
    else:  #第四象限
        coordinate_x = cos(angle_in_radians) * length
        coordinate_y = -sin(angle_in_radians) * length
    print ' ( X , Y ) = ( %.3f , %.3f )' % (coordinate_x,coordinate_y)
    return coordinate_x,coordinate_y

print '第三題 :'
findXY(10,120)


#4.
def findAngle(angle1,angle2):
    Angle = angle1-angle2
    if Angle > 0:
        dd2dms(Angle)
        return Angle
    elif Angle <= 0 :
        Angle = -Angle
        dd2dms(Angle)
        return Angle

    print ' Angle between the two vectors = %.5f' % Angle
    
print '第四題 :'
findAngle(410,136.894)






#5.
def dd2rad(degrees):
    radians = degrees * pi / 180 #角度轉換成弧度攻勢
    print ' %.5f Degrees = %.5f Radians ' % (degrees,radians)
    return radians

print '第五題 :'
dd2rad(360)



#6.
def rad2dd(radians):
    degrees = radians * 180 / pi
    print ' %.5f Radians = %.5f Degrees' % (radians,degrees)
    return degrees

print '第六題 :'
rad2dd(6.28319)


#7.
def distance(length1,angle1,length2,angle2):
    coordinate1_x, coordinate1_y = findXY(length1,angle1)
    coordinate2_x, coordinate2_y = findXY(length2,angle2)
    distance = sqrt( (coordinate1_x - coordinate2_x)**2 + (coordinate1_y - coordinate2_y)**2 )
    print ' Distance between ( %.3f , %.3f ) and ( %.3f , %.3f ) = %.5f' % (coordinate1_x,coordinate2_x,
                                                                           coordinate1_y,coordinate2_y,distance)
    return distance

print '第七題 :'
distance(20,30,10,60)


print '--------------------第二大題--------------------'


#第二大題
#1. A(3,4) , B(8,16)
point = {'A' : (3,4), 'B' : (8,16)}  #Practicing function with **kwargs
def dis(**points):  
    distance = sqrt( (points['A'][0] - points['B'][0])**2 + (points['A'][1]-points['B'][1])**2 )
    print ' Distance between A(3,4) and B(8,16) = %.4f' % distance
    return distance

print '第一題 :'
dis(**point)


points = [(3,4),(8,16)]
def distant(*args): #Practicing function with *args
    distance = sqrt( (args[0][0]-args[1][0])**2 + (args[0][1]-args[1][1])**2 )
    print ' Distance between A(3,4) and B(8,16) = %.4f' % distance
    return distance

distant(*points)


#2.
def B_coordinate():
    ab_distant = 5
    ab_angle = 30
    ab_radian_angle = ab_angle*pi/180
    coordinate_x = ab_distant*sin(ab_radian_angle)
    coordinate_y = ab_distant*cos(ab_radian_angle)
    print ' The coordinate of point B is ( %.6f , %.6f )' % (coordinate_x,coordinate_y)
    return coordinate_x , coordinate_y

print '第二題 :'
B_coordinate()


#3.
def avg():
    observation = [180.0546, 180.0566, 180.0489, 180.0498, 180.0557]
    answer = sum(observation)
    # or , another more tiring method\
    s = 0
    for o in observation:
        s= s+0
    answerr = s / len(observation)
    print ' The Average of the observation = %f' % answer
    return answer

print '第三題 :'
avg()


#4.
def B_height(height,front_vision,back_vision):
    height_difference = back_vision - front_vision
    B_height = A_height - height_difference
    return B_height



A_height = 23.516
front_vision = 170.265
back_vision = 145.289

print '第四題 :'
b_height = B_height(A_height,front_vision,back_vision)
print ' Height of B = %.5f' % b_height


#5.
T1 = B_height(17.524,153.217,142.758)
T2 = B_height(T1,176.458,152.418)
b_height = B_height(T2,142.718,137.569)

print '第五題 :'
print ' Height of B = %.5f' % b_height


def check_int_input(s , input_value):
    ti = 0
    try:
        input_value = float(input_value)
    except Exception as e:
        print 'BUG____------>' , e
        print 'You CAN\'T type in anything other than the integers of those choices yo!'
        ti = 1
    while ti == 1:
        input_value = raw_input(s)
        ti = 0
        try:
            input_value = float(input_value)
        except Exception as e:
            print 'BUG---> ' ,e
            print 'You CAN\'T type in anything other than the integers of those choices yo!'
            ti = 1
    return input_value

l = [option for option in range(1,8)]

while True:
        s = '使用者自行使用第一大題\n(選擇題目--->[1] dd2dms(degrees) , [2] dms2dd(circumference = 0, degree = 0 , minute = 0, second = 0),\
[3] findXY(length,angle) , [4] findAngle(angle1,angle2) , [5] dd2rad(degrees) , [6] rad2dd(radians) , [7] distance(length1,angle1,length2,angle2)) \
\n -----> : '
        a = raw_input(s)
        a = check_int_input(s , a)
        if a not in l:
            print 'Since you can\'t understand that there are only three choices, guess i\'ll choose for you!'
            a = random.randint(1,7)
        if a == 1:
            print '第一題:'
            s = 'Enter Decimal Degrees to be converted: '
            degrees = raw_input(s)
            degrees = check_int_input(s , degrees)
            dd2dms(degrees)
        if a ==2:
            print '第二題:'
            print 'Enter (IN ORDER!), circumference , degree , minute , second  (By default it all = 0), to be converted into decimal degrees: '
            s = 'Enter circumference : '
            circumference = raw_input(s)
            circumference = check_int_input(s,circumference)
            s = 'Enter degree : '
            degree = raw_input(s)
            degree = check_int_input(s, degree)
            s = 'Enter minute : '
            minute = raw_input(s)
            minute = check_int_input(s, minute)
            s = 'Enter second : '
            second = raw_input(s)
            second = check_int_input(s, second)
            dms2dd(circumference , degree , minute , second)
            
        if a == 3:
            print '第三題:'
            print 'Enter Length and Angle to find the coordinates: '
            s = 'Enter Length : '
            length = raw_input(s)
            length = check_int_input(s , length)
            s = 'Enter Angle : '
            angle = raw_input(s)
            angle = check_int_input(s , angle)
            findXY(length , angle)


        if a == 4:
            print '第四題:'
            print 'Enter 2 angles to find the value of their differences: '
            s = 'Enter angle 1 : '
            angle1 = raw_input(s)
            angle1 = check_int_input(s , angle1)
            s = 'Enter angle2 : '
            angle2 = raw_input(s)
            angle2 = check_int_input(s , angle2)
            findAngle(angle1 , angle2)
            
        if a == 5:
            print '第五題:'
            s = 'Enter Degrees to convert its values to radians: '
            degrees = raw_input(s)
            degrees = check_int_input(s , degrees)
            dd2rad(degrees)
            
        if a == 6:
            print '第六題:'
            s = 'Enter Radians to convert its values to degrees: '
            radians = raw_input(s)
            radians = check_int_input(s , radians)
            rad2dd(radians)
        
        if a == 7:
            print '第七題:'
            print 'Enter Length1 ,Angle1 and Length2 , Angle2 to find the distance between two points: '
            s = 'Enter Length1 : '
            length1 = raw_input(s)
            length1 = check_int_input(s , length1)
            s = 'Enter Angle1 : '
            angle1 = raw_input(s)
            angle1 = check_int_input(s , angle1)
            s = 'Enter Length2 : '
            length2 = raw_input(s)
            length2 = check_int_input(s , length2)
            s = 'Enter Angle2 : '
            angle2 = raw_input(s)
            angle2 = check_int_input(s , angle2)
            distance(length1,angle1,length2,angle2)
            
        
        z = raw_input("Still want to play?(Press [N] or type in [NO] to quit\
, else type in whatever to keep on going~): ")
        z = z.upper()
        if z == 'N' or z == 'NO':
            print'Good Bye, Have a nice day~~~!!!'
            break
        else:
            pass
   

