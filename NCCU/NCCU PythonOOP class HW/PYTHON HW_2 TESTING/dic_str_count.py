def pic(s):
    d = dict()
    for c in s:
        c = c.lower()
        d[c] = 1 + d.get(c , 0)

    return d

print(pic("Kiss my little ASS you BITcH!!!! mother FUCKERRRR !!! YOlo!"))
