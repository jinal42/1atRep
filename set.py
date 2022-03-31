print("--- set ---")

myset={'s1','s2','s3','s4','s5'}
print(myset)

myset1=len(myset)
print(myset1)

print(type(myset))

'''myset2=myset.count("s1")
print(myset)
'''
for s in myset:
    print(s)

print('s2' in myset) #myset set name . and to check s2 in given set
num_set={1,2,3,4,5}
print(2 in num_set)
print(0 in num_set)

num_set.add(7)
print(num_set)

s11={1,2,3,'a'}
s22={'a','b','c',1,3}
s11.update(s22)
print("update set : ",s11)

#s0=s11.union(s22)
#print("union set : ",s0)



s12={'cat','dog'}
s12.add("goat") #add item in set
print(s12)
s21=['cow','donkey']
s12.update(s21)
print("update list and set ",s12)

s12.remove("cat")
print("remove (remove())'cat' in set of s12 :",s12)

s12.discard("cow")
print("remove (discard()) 'cat' in set of s12 :",s12)

s12.pop()
print(s12) # remove last element of the set

s15={2,4,3,5,7,9}
print(s15)

s133=s15.pop()
print(s133)
print(s15)

s15.clear()
print("clear() set :",s15)

x1={'purple','red','pink'}
x2={'white','blue','purple'}
x1.intersection_update(x2)
print(x1) #The intersection() method will return a new set, that only contains the items that are present in both sets.

x3={1,4,5,11}
x4={0,1,5,9}
x3.symmetric_difference_update(x4)
print(x3)

x7={1,4,5,11}
x8={0,1,5,9}
x9=x7.symmetric_difference(x8)
print(x9)


