#codecademy practice
#censor_string
def censor(text,word):
    if word in text:
        text = text.replace(word,"*"*len(word))
        print(text)
    else:
        print(text)

censor("teemo must die", "teemo")
