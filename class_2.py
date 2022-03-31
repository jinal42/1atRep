"""class stud:
    pass
s1=stud()
s2=stud()

s1.name="harry"
s1.std=12
s1.section=1

s2.name="larry"
s2.std=9
s2.sub=["python","php","android"]

print(s1,s2)
print(s1.name,s1.section)
print(s1.std)

print(s2.name,s2.sub)"""

class emp:
    no_of_leaves=7
    pass

harry=emp()
larry=emp()

harry.name="harry"
harry.sal=4500
harry.role="employee"

larry.name="larry"
larry.sal=6000
larry.role="instructor"

print(harry.name)
print(harry.role)

print(emp.no_of_leaves)
#emp.no_of_leaves=1
larry.no_of_leaves=1

print(emp.no_of_leaves)
print(larry.no_of_leaves)


print(larry.__dict__)
print(emp.__dict__)

emp.no_of_leaves=10
print(emp.__dict__)




