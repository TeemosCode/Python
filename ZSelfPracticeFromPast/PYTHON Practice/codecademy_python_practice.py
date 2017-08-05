#codecademy python practice

#factorial(階層)
#using a dumb list way
def factorial(x):
    ls = []
    s = 1
    for n in range(x):
        ls.append(n+1)
    for x in ls:
        s = s * x
    return s

#try calling the function itself
def factorial(x):
    s = x
    if x > 0:
        s = s * factorial(x-1)
    else:
        return 1
    return s

factorial(5)
