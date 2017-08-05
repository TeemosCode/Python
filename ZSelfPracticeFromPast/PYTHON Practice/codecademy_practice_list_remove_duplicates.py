#codecademy practice
#remove_duplicates_list
def remove_duplicates(ls):
    nls = []
    for x in ls:
        if x in nls:
            pass
        else:
            nls.append(x)
    print(nls)

remove_duplicates([11,22,11,22,12,31,24,345,11,22,33433,12,12,12,'我我',"我","我","我","我我"])
