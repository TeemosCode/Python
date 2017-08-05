import random
def createData(minium, maximum , n):
    ls = []
    for i in range(n):
        ls.append(random.randint(minium , maximum))
    ls.sort()
    print(ls)
    return ls


def getStats(data):
    data.sort()
    Data = {}
    Data["minimum"] = min(data)
    Data["maximum"] = max(data)
    s = 0
    for n in data:
        s = s + n
    Data["mean"] = s
    if len(data) % 2 == 1:
        Data["median"] = data[(len(data)//2)]
    else:
        Data["median"] = (data[(len(data)//2)] + data[(len(data)//2 -1)])/2

    print(Data)
    return Data


def classifyData(data):
    dic = {}
    count = 0
    for x in data:
        count = count + 1
        if x >= 90:
            dic["A"] = dic.get("A",0) + 1
        elif 80 <= x < 90:
            dic["B"] = dic.get("B",0) + 1
        elif 70 <= x < 80:
            dic["C"] = dic.get("C",0) + 1
        elif 60 <= x < 70:
            dic["D"] = dic.get("D" , 0) + 1
        else:
            dic["F"] = dic.get("F", 0) + 1
    print("There are total:" , count , "of Data"  )
    print(dic)
    return dic


def printData(data , n):
    data.sort()
    if n > 0:
        print(data[:n])
    else:
        print(data[n:])


createData(300 , 750 , 10)
getStats([1,2,3,4,5,6])
classifyData([61,80,70,76,74,23,45,76,87,90,89,98,66,43,57,68,87,98,90,99,100,76,67,56,68,69,2,45,35,43,57,76,61,63,62,71,77,74,83,86,99])
printData([6,4,6,5,6,6,66,77,3456,123,645,90] , -5)



