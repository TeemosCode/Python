
#py259_何秉哲_hw5

class student:
    def __init__(self , name, gender):
        self.name = name
        self.gender = gender
        self.grades = []
        
    def avg(self):
        sm = 0
        for x in range(len(self.grades)):
            sm = sm + self.grades[x]
        average = sm / len(self.grades)
        return average
    
    def add(self , grade):
        self.grades.append(grade)
        
    def fcount(self):
        fg = 0
        for x in range(len(self.grades)):
            if self.grades[x] < 60:
                fg += 1
        return fg       

def top(stds):
    a = []
    for avg in range(len(stds)):
        a.append(stds[avg].avg())
    for mx in range(len(a)):
        if a[mx] == max(a):
            return stds[mx].name
         
    
    





s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)

students = (s1, s2 , s3 , s4 , s5)

print("%s ( %s ) , Average: %.2f , Failed:  %i  courses." % (s1.name , s1.gender , s1.avg() , s1.fcount()) )
print("%s ( %s ) , Average: %.2f , Failed:  %i  courses." % (s2.name , s2.gender , s2.avg() , s2.fcount()) )
print("%s ( %s ) , Average: %.2f , Failed:  %i  courses." % (s3.name , s3.gender , s3.avg() , s3.fcount()) )
print("%s ( %s ) , Average: %.2f , Failed:  %i  courses." % (s4.name , s4.gender , s4.avg() , s4.fcount()) )
print("%s ( %s ) , Average: %.2f , Failed:  %i  courses." % (s5.name , s5.gender , s5.avg() , s5.fcount()) )

print("平均分數最高者: %s" % top(students))


