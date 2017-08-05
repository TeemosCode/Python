#codecademy practice
#product_list
def product(ls):
    r = 1
    if len(ls) > 0:
        for n in ls:
            r = r * n
        print(r)
    else:
        r = 0
        print(0)

product([])
