#codecademy practice
#list_median

def median(ls):
    ls.sort()
    print(ls , "\n")
    if len(ls) % 2 == 1:
        print(ls[len(ls)//2])
    else:
        print( ( ls[len(ls)//2] + ls[len(ls)//2 -1] ) / 2 )



median([4,5,5,4])
