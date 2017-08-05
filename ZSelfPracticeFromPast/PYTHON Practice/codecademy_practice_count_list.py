#codecademy practice
#count_list
def count(sequence,item):
    s = 0
    for i in sequence:
        if item == i:
            s = s+1
        else:
            pass
    if s > 0:
        print(s)
    else:
        print(0)

count([123,123,7,'asfd',123] , 123)
