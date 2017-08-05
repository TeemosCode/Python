#102306061_03 何秉哲 HW_3  (讀取 DMC 航空攝影記錄資料，建立 SQLite 資料庫)

file = open("150814DMCabstop.sel" , "r" , encoding = "UTF-8")
doc = open("SQLite_database" , "w" , encoding = 'UTF-8')


doc.write("%12s"%"NAME" + "%12s"%"E" + "%12s"%"N" + "%9s"%"H" + "%11s"%"E"
              + "%10s"%"N"+ "%10s"%"H" + "%12s"%"DATE\n")

s= 0
for line in file:
    s += 1
    if s == 1 or s == 2:
        pass
    elif s != 1 and s != 2:
        l = line.split()
        doc.write( "%s_%s %s %s %s %s %s %s %s\n"%(l[0] , l[1] , l[2] , l[3], l[4], l[5] , l[6] , l[7] , l[9]) )


file.close()
doc.close()


