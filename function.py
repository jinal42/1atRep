def my_first():
    print("my 1st function...")
my_first()
print()

def f1(x):
    print("subject :",x)
f1("python")
f1("php")
f1("c++")
print()


def f1(x):
    print(x)
f1("python")
f1("php")
f1("c++")
print()

def f2(*sub):
    print("subject : ",sub[3])
f2("python","c","php",'c++')
print()

def f3(a,b,c):
    print(c)
f3(a='one',b="two",c="three \n")

def num(a,b):
    print(b)
num(a="a",b='b\n')


def fun(**num):
    print(num['four'])
fun(one="book",two="pen",three="cup",four="toy")
print()


def my_city(city="surat"):
    print(city)
my_city("vapi")
my_city("baroda")
my_city()
my_city("navsari \n")



animal_lst=['cat','dog','cow']
def lst(f):
    for x in f:
        print(x)
lst(animal_lst)
print()

vegi_lst=\
    ['carrot','radish']
def lst2(root_vegi):
    for y in root_vegi:
        print(y)
lst2(vegi_lst)


def math_fun(m):
    return m ** 2
print(math_fun(4))
print(math_fun(11))
print(math_fun(23))

print("this is pycharm",end=" ")
print("editor")

print("c",end=" and ")
print("c++")

print("python "*10)

