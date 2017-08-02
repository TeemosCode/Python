#Homework 3

# for 迴圈

n = int(input(" Input a number: "))


while n <= 0:# 因為自己試過負數和0不會有任何回傳結果 ( 不知道原因，可能需要請教老師 ) ，以while迴圈讓輸入小於等於0的使用者繼續輸入直至輸入值為大於0之正整數
    print('sorry can\' print this out , I\'m still a beginner at coding so I can\' explain why , please print out a number greater than zero: ')
    n = int(input(" Input a number: "))
    if n > 0:
        break
    
# 作業答案(for迴圈)

for x in range(1 , n+1):
    for y in range(1 , n+1):
        print( x * y )
    


    

        
# while 迴圈

z = int(input("Input a number: "))


while z <= 0:# 因為自己試過負數和0不會有任何回傳結果 ( 不知道原因，可能需要請教老師 ) ，以while迴圈讓輸入小於等於0的使用者繼續輸入直至輸入值為大於0之正整數
    print('sorry can\' print this out , I\'m still a beginner at coding so I can\' explain why , please print out a number greater than zero: ')
    z = int(input(" Input a number: "))
    if z > 0:
        break

#作業答案(while迴圈)

num1 = 1
num2 = 1
while num1 <= z:
    while num2 <= z:
        print( num1 * num2)
        num2 += 1
    num2 = 1
    num1 += 1
