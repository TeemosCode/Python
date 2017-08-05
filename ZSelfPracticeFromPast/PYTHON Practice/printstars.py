#printstars

'''

*
**
***
****
*****

'''
def printstars(n):
    for i in range(1 , n+1):
        print("%s" % ("*"*i))






printstars(5)

print("---------------------")

def printstars2(n):
    for i in range(1 , n+1):
        print( "%s" % ( "*"* (n+1-i) ) )

printstars2(5)

print('----------------------')

'''
#print中加，會多出一格(為啥啊?!!!!!!!!!!!!!!)
def printstars3(n):
    for i in range(1 , n+1):
        print( ( (n-i) * " " ), "%s" % ("*"*i)) 

printstars3(5)
'''
def printstars3(n):
    for i in range(1 , n+1):

            print(((n-i) * " " ) + "%s" % ("*"*i)) 
       
printstars3(5)

print("-------------------------------" )

def printstars4(n):
    for i in range(n):
        print((i*" ")+(n-i)*"*")

printstars4(5)
    
