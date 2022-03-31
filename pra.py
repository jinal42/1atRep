"""n1=int(input("enter 1st num:"))
n2=int(input("enter 2st num:"))
#print("1st num is :",n1,"and 2nd num is :",n2)
print("sum of ",n1,"and" ,n2 ,"is :",n1+n2)
"""


"""
p=int(input("enter product price :"))
txt="product price is : {}"
print(txt.format(p))
"""

p=49
txt="number :- {}"
print(txt.format(p))

p1=23
txt1="num : {:.2f}"
print(txt1.format(p1 ))


name='python'
year=1998
txt="my name {} and i m {} old"
print(txt.format(name,year))

str="rose is {3} apple is {0} hair is {2} and lemon is {1} total item {5} and amt {4}"
a= 'red'
r='pink'
h='black'
l='yellow'
i=4
amt=100
print(str.format(a,l,h,r,amt,i))

str1="rose is {} apple is {} hair is {} and lemon is {} total item is {} and amount {:.2f}"
a1= 'red'
r1='pink'
h1='black'
l1='yellow'
i1=4
amt1=100
print(str1.format(r1,a1,h1,l1,i1,amt1))

car="my car name is {carname} and model is {model}"
print(car.format(carname="abc",model="mustang"))

