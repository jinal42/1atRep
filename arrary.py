

a1=[1,12,30,24,5]
print(a1)

print(a1[2])

a1[0]=100
a1.append(89)
print(a1)

print(len(a1))

for a in a1:
    print(a)

print(a1.pop())
print()

a1.remove(100)
print("remove : ",a1)

a1.sort()
print("sort : ",a1,"\n")


li=[1,2,34,56,78,0,9,0]
print(li.count(0))

lis=['cat','dog','cow','dog','fish']
print("dog : ",lis.count("dog"))
print("fish : ",lis.count("fish"))
print("duck : ",lis.count("duck"))


l1=[110,12,3,40]
l2=['cat']
l1.extend(l2)
print("extend l1 and l2 :",l1)

l1.insert(2,'dog')
print(l1)

l1.pop(3)
print(l1)

l1.pop(4)
print(l1)

'''def fun(f):
    return f['clr']
list1=['red','green','pink',white]
fun(f=list)

fun.sort(key=list1)'''