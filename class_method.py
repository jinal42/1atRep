class emp:
    no_of_leaves=12
    def __init__(self,name,sal,des):
        self.n=name
        self.s = sal
        self.d=des
    def details(self):
        print(f"name : {self.n} , salary {self.s} , desg : {self.d}")

    @classmethod
    def change_l(cls,new_l):
        cls.no_of_leaves=new_l

e1=emp("harry",29000,"employee")
e2=emp("rohan",6000,"student")
e1.details()
e2.details()

print(e2.no_of_leaves)

emp.no_of_leaves=9
print(e2.no_of_leaves)

e2.change_l(2)
print(e2.no_of_leaves)


"""
print(e1.n)
print(e1.s)
print(e1.d)
"""