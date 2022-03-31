class mycls:
    x=10
    y=90
    z='python'

p=mycls()
print(p.x)
print(p.y)
print(p.z)
print()



class person:
    def __init__(self,sub,code):
        self.sub=sub
        self.code=code
p1=person("pthon",101)
print(p1.sub)
print(p1.code)
print()


class stud:
    id=1
    stud_id='ER101108'
s=stud()

print(s.id)
print(s.stud_id)
print()



class stud1:
    def __init__(self,stdID,stdENROLL):
        self.stdID=stdID
        self.stdENROLL=stdENROLL
s1=stud1(1,"ER101")
s2=stud1(2,"ER102")
s3=stud1(3,"ER103")

print(s1.stdID,s1.stdENROLL)
print(s2.stdID,s2.stdENROLL)
print(s3.stdID,s3.stdENROLL)
print()



'''class c1:
    def __init__(self,name,age,clr):
        self.name=name
        self.age=age
        self.clr=clr
    def myfun(self):
        print(self.name , self.age,self.clr)
clss=c1("jinal",22,"purple")
clss1=c1("riddhi",17,"pink")

clss.myfun()
clss1.myfun()'''

class c1:
    def __init__(sl,name,age,clr):
        s.n=name
        s.a=age
        s.c=clr
    def myfun(sl):
        print(s.n , s.a,s.c)
clss=c1("mitu",22,"purple")
clss.age=23
print(clss.age)
'''del clss.age
print(clss.age)
'''

clss.myfun()

class no_body:
    pass


