
#py259_何秉哲_hw6


file1 = open('stores_old.csv', mode = 'r' )
file2 = open('stores_new.csv', mode = 'w' )

def countlines(file1 , file2):
    
    for line in file1.readlines():
        file2.write( line.split(",")[0] + line.split(",")[3] + line.split(",")[5] + line.split(",")[6] + '\n')
    return file2

countlines(file1, file2)
file1.read()

file1.close()
file2.close()



    
    
