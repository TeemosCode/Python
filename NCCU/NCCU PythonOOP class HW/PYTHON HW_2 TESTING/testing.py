file = open('hw2_data.doc', mode = 'r')
result1 = open('hw2_result.doc', mode = 'w')

frstn = []
lstn=[]
stdid=[]
avgs=[]

def count_averges(avgs):
    file = open('hw2_data.txt', mode = 'r')
    for line in file.readlines():
        s = 0
        w = 0
        avg = 0
        for i in line.rstrip().split(' ')[3:18:2]:
            i = int(i)
            s = s + i
        for x , y in zip(map(int , line.rstrip().split(' ')[3:18:2]) , map(int ,line.rstrip().split(' ')[4:19:2])):
            w = w + x*y
        avg = w / s
        avgs.append(avg)
    file.close()
    return avgs


    


def make_lastname_list(lstn):
    file = open('hw2_data.txt', mode = 'r')
    for line in file.readlines():
        lstn.append(line.rstrip().split(' ')[0])
    file.close()   
    return lstn



def make_firstname_list(frstn):
    file = open('hw2_data.txt', mode = 'r')
    for line in file.readlines():
        frstn.append(line.rstrip().split(' ')[1])
    file.close()
    return frstn

def make_student_id(stdid):
    file = open('hw2_data.txt', mode = 'r')
    for line in file.readlines():
        stdid.append(line.rstrip().split(' ')[2])
    file.close()
    return stdid

 
def sort_with_name(frstn, lstn, stdid, avgs):
    l = []
    a = zip(frstn , lstn , stdid, avgs)
    for frstn , lstn , stdid, avgs in a:
        l.append((lstn , frstn , stdid, avgs))
    l.sort()
    print("以姓名排序，由大到小排列。排序為；姓名、學號、學期平均成績 ： " + '\n')
    for a ,b ,c ,d in l:
        print(a , b , c , d)
        
    


make_student_id(stdid)
make_firstname_list(frstn)
make_lastname_list(lstn)
count_averges(avgs)

print("102306061  資管三甲  何秉哲  HW_2" + '\n' + '\n' + '\n')
#sort_with_score(frstn , lstn , stdid, avgs)

#sort_with_id(frstn, lstn, stdid,avgs)

sort_with_name(frstn, lstn, stdid, avgs)

file.close()
result1.close()