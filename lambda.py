l= lambda a:a+2
print(l(2))

l1 = lambda a : a/2
print('a/2 :',l1(14))

l1 = lambda a : a * 2
print("a * 2 : ",l(2))

a= lambda a,b,c : a*b*c
print('a * b * c :',a(2,5,2))

def my_lambda(t):
    return lambda n:n+t
x=my_lambda(1)
print(x(10))
print()


def my_lambda(t):
    return lambda n:n+t
x=my_lambda(1)
y=my_lambda(2)

print(x(14))
print(y(10))