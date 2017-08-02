#WEEK1 HOMEWORK
#Q1
print("Q1\n")

Mp = {'Tom' , 'John' , 'Mary' , 'Jimmy' , 'Sunny' , 'Amy'} # 數學及格者(Math passed)
Ep = {'John','Mary','Tony','Bob','Pony','Tom','Alice'} # 英文及格者(English passed)

MpEf = Mp - (Mp&Ep)#數學及格但英⽂不及格的名單
MfEp = Ep - (Mp&Ep)#數學不及格但英⽂及格的名單
MpEp = Mp & Ep#兩科都及格的名單
MaEa = Mp|Ep#全班的同學名單



print( "數學及格但英⽂不及格者 : "  , MpEf)
print("數學不及格但英⽂及格者 : " , MfEp)
print("兩科都及格者 : "  , MpEp)
print( "全班總共有: " , len(MaEa) , "位同學\n")


#Q2
print("Q2\n")

TP = [80, 100, 90, 95]#Tom's Points
JP = [100,93,75,80]#John's points

grades = {'Tom' : TP , 'John' : JP }#dict型態 存放兩個同學的資料

print(grades)

TA = (TP[0] + TP[1] + TP[2] + TP[3]) / len(TP)#Tom's Average
JA = (JP[0] + JP[1] + JP[2] + JP[3]) / len(JP)#John's Average

print( "Tom's Average : " , TA )
print( "John's Average: " , JA , '\n')
