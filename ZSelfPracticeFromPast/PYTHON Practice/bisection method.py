#determines the root of f(x) = x^3 - x - 2 by using Bisection algorithm
#############dammmmmn only integer roots OMG!!!!
def bisec():
    n = int(input("what root do you think? :"))
    x = n
    print("x**3 - x - 2 = " , n**3 - n - 2)
    while (n**3 - n - 2)!= 0:
        n = int(input("what root do you think? :"))
        if (x**3 - x - 2) * (n**3 - n - 2) < 0:
            print("choose a number between %d and %d :" % (x , n))
            x = n
        elif (x**3 - x - 2) * (n**3 - n - 2) > 0:
            print("choose a number thats a bit more different than %d and %d :" % (x , n))
            x = n
        else:
            print("%d is the root! " % n)
            return
    print("%d is the root" % n)


bisec()
