file1 = open('stores_old.csv', mode = 'r' )
file2 = open('stores_new.csv', mode = 'w' )


for line in file1.readlines():
    print(line)
