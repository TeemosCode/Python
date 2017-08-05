import random

def my():
    c = 0
    for x in range(100):
        n = random.randrange(1,1001,2)

        print(n)
        c += 1

            
            
    print("this is :" , c)

def teachers():
    odd_nums = range(1,1000,2)
    for num in random.sample(odd_nums,100):
        print(num, file=open('random.txt', "a"))
