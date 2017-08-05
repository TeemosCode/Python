#codecademy practice
#purify_list
def purify(ls):
    even = []
    for n in ls:
        if n % 2 == 0:
            even.append(n)
        else:
            pass
    print(even)

purify([1,2,34,5,6,123,4,5,6,7,7,3,456,2,2,8,9,2450,60,5487,54,54,455])
