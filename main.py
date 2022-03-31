# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

t2=[12,'male',12.0,True]
print('diff. datatype in list',t2)

tup=('pyhton','java','c++','c','php')
print('diff. datatype in tuple',tup)
print("tuple length : " , len(tup))
print("tuple type : ",type(tup))

print("convert 'z' to 'b' ")
a=('a','z','c','d')
print(a)
b=list(a)
b[1]='b'
a=tuple(b)
print(a)


t2=(1,2,3,4,5)
print("t2 tuple : ",t2)
m=list(t2)
m.append(6)
t2=tuple(m)
print("append :",t2)

t4=(1,2,0,4,5)
print("t4 tuple : ",t4)
n=list(t4)
n.remove(0)
t4=tuple(n)
print("remove :",t4)

t3=(7,8)
y=(9,10)
t3=t3+y
print("append tuple :",t3)

'''del_tup=(1,2,3)
del del_tup
print(del_tup)'''

print("packing and unpacking tuple")
p_t=("a","b","c")
(x,y,z)=p_t
print(x)
print(y)

f=('banana','mango','lichi','apple','orange')
(yellow,*red,orange)=f
print(yellow)
print(red)
print(orange)


for a in f:
    print(a)

"""r=range(1,22,5)
for x in r:
    print(x)"""



r1=range(3)
for y in r1:
    print(y)


r1=range(3)
print("reverse range :")
for y in reversed(r1):
    print(y)

r2=range(5,100,25)
for y in r2:
    print(y)

r3=range(1,-21,-4)
for t in r3:
    print(t)

f=('p','q','r','s','t')
i=0
while i < len(f):
    print(f[i])
    i+=1

f2=('p','q','r','s','t','a','p','c')
print("use of count() :")
f3=f2.count('p')
print(f3)

f4=f2.count('d')
print(f4)

f0=len(f2)
print('total no of item in f2 tuple :',f0)

print("use of index() :")
f6=(0,45,12,99,85,47)
f6=f6.index(85)
print(f6)


str="String is  Slicing and Other  Functions in Python"
str1="pyhton admin 123 pass root"
print(str1.find("123"))
print(str[::-1])
print(str.isalnum())
print(str.endswith("Python"))

"""Hi GSO,

Following are the updates for GSO as on 29th March, 2022 :

List of Completed Tasks :
self() and __init() constructor [Done]
user input [Done]
string formatting [Done]
instances and class variables [Done]
escape character [Done]
List of In-Progress Tasks :
inheritance
List of Remaining Tasks :
dates
Please check with the latest updates and let us know your thoughts for the same.

Thanks,
GSO """