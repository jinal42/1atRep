"""import datetime

x = datetime.datetime.now()

print(x.year)
print(x.day)
print(x.timetz())
"""

import datetime
import time

d=datetime.datetime.now()
print(d)




i1=time.time()
#print(i1)

for y in range(20):
    print(y)
print("i1 ",time.time() - i1)

i3=time.time()
#print(i3)

for x in range(20):
    print(x)
print("i3 ",time.time() - i3)



"""i=time.time()
print(i)
j=0
while (j<20):
    print(j)
    j+=1
print("2st ",time.time() - i)"""
