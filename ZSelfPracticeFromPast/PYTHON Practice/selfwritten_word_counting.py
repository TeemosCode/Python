# counting file words
name = input("which file to count words? :")
file = open("name" , "w" , encoding = "UTF-8")

start = input("word to start with :")
end = input("word to end with :")
row = int(input("input how much rows to count :"))


sm = 0
rows = 0
count = 0
for line in file:
    if start in line and count == 0:
        count += 1
        for line in file:
            rows += 1
            for word in line:
                sm += 1
                if rows == row and word == end:
                    sm += 1
                    break
            break
        break
    break

print(" ' %d ' words" % sm)
                    

                
             
                
