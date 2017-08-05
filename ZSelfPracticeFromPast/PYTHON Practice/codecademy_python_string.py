#codecademy python practice
#reverse string
def reverse(text):
    l = len(text)-1
    s = text[l]
    for i in range(len(text)-1):
        if l > 0:
            s = s + text[l-1]
            l -= 1
        else:
            break
    print(s)
    
reverse("string@yo#yalo")
