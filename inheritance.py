"""class emp:

    def __init__(self,name,sal,des):
        self.n=name
        self.s=sal
        self.d=des
    def details(self):
        print(f"name : {self.n} , salary {self.s} , desg : {self.d}")


class programmer(emp):
    def __init__(self,name,sal,des,lun):
        self.n=name
        self.s=sal
        self.d=des
        self.l=lun

    def prog_details(self):
        print(f"programmer name : {self.n} , salary {self.s} , desg : {self.d},{self.l}")


e1=emp("harry",29000,"employee")
e2=emp("rohan",6000,"student")

e3=programmer("e3",5000,"programmer",["php","android"])
e4=programmer("e4",3500,"programmer",["python","cpp"])

print(e2.details())

print(e4.prog_details())

#print(e4.prog_details())
#print(e4.details())
"""

b={}
l1={"abc":1}
l3={1:1}
b.update({"str":4})
l3.update(l1)
print(b)
print(l3)

d={"abc":1,"xyz":2,"pqr":3}
a={}
jinal_op=[{"abc":1,"xyz":2,"pqr":3}]
j=[]
for key, value in d.items():
    a.update({key:value})
    j.append(a)
print("testing a dict", a)
print("-********* jinal ***********",j)
"""
dict1={1:1,2:2}
d=dict(dict1)
print(d)"""