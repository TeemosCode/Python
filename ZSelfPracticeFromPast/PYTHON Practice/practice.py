def reverse(text):
    
    l = len(text) - 1
    s = text[l]
    if l >= 0:
        for x in range(len(text)-1):
            s = s + text[l-1]
            l -= 1
        print(s)
    else:
        print(s)

reverse("teemo")
