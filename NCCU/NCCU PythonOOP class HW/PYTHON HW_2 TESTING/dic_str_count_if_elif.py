def pic(s):
    d = dict()
    for c in s:
        c = c.lower()
        if c not in d:
            d[c] = 1
        elif c in d:
            d[c] += 1

    return d

print(pic("Kiss my little ASS you BITcH!!!! mother FUCKERRRR !!! YOlo!"))
