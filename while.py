i=11
while i <=15:
    print(i)
    i+=1
print()
j=9
while j>=3:
    print(j)
    j=j-1

print()

k=0
while k<=10:
    print(k)
    if k == 4:
        break
    k+=1
print()


c=10
while c<=17:
    c += 1
    if(c==13):
        continue
    print(c)
print()
#-------
l=0
while l<5:
    l+=1
    if(l==3):
        continue
    print(l)


print()
e=21
f=27
while e <f:
    print(e)
    e+=1
else:
    print("no long than ",f)

print()

list=[1,2,3,4,5]
for x in list:
    print(x)
print()

for q in "jinal":
    print(q)
print()

no=[1,2,3,4,5,6]
for x in no:
    print(x)
    if(x==4):
        break

print()
no1=[45,78,84,56,65,7]
for x in no1:
    print(x)
    if(x==56):
        continue

for x in range(6):
    if(x==3):
        break
    print(x)
print()

a=[1,2,3]
b=['a','b','c','d']
for x in a:
    for y in b:
        print(x,y)