#codecademy python practice
#Vowels~~~
'''
'c' in "aeiouAEIOU"
False
''' 
        
def anti_vowel(text):
    count = 0
    for c in text:
        count += 1
        if c not in "aeiouAEIOU":
            s = c
            break
        else:
            pass
    if count == len(text):
        print("All vowels yo!!")
        return
    else:
        for ch in text[count:]:
            if ch not in "aeiouAEIOU":
                s = s + ch
            else:
                pass
    print(s)

anti_vowel('Hey You!')
            
