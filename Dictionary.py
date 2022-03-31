dic={'apple':'red','banana':'yellow','cherry':'pink','watermelon':'green' }
print(dic)

print(dic["banana"])

dic1={'apple':'red','watermelon':'green','banana':'yellow','cherry':'pink','watermelon':'pink' }
print(dic1)  #Dictionaries cannot have two items with the same key:


print("dictionary length :",len(dic))

num={1:'one','two':2}
print(num)

mix_dic={1:'a',"clr":['red','green'],'yes':True}
print(mix_dic)

print(type(mix_dic))

print(dic['apple'])
print(dic.get("banana"))

print("dictionary key :",dic.keys()) #keys() method will return a list of all the keys in the dictionary.
"""k=dic.keys()
print(k)"""

dic["chikuu"]="brown"
print(dic.keys())

z=dic.values()
print(z)

get_val={'color':'purple',"subject":"python","site":"w3 school"}
j=get_val.values()
print(j)
get_val["color"]="orange"
print(j)
get_val['year']=2022

print(j)

item1={1:'one',2:'two',3:'three'}
i=item1.items()
print(i)


dic2={'a':'apple','b':'bat','c':'cat','f':"fish",'g':'goat'}
dic3={'sky':'blue',"sun":'yellow',"hair":"black"}

if "sky" in dic3:
    print("yes")
else:
    print("no")

if "blue" in dic3:
    print("yes")
else:
    print("no")
dic3["hair"]="brown" #change dictionary value
print(dic3)

print("dic2 before adding item",dic2)
dic2['d']="dog"
print("dic2 after adding item",dic2)

dic2.update({"d":"doll"})
print("update value of 'd'(dog to doll) : ",dic2)

#dic2.pop("b")
#print(dic2)

dic2.popitem()
print(dic2)

del dic2["g"] # delete 'g'
print(dic2)

dic2.clear()
print(dic2)

for d in dic3: #retrive dictionary key
    print(d)

for d in dic3: #retrive dictionary value
    print(dic3[d])

print("keys() and values() using loop :")
for d in dic3.values():
    print(d)

for d in dic3.keys():
    print(d)

for k,v in dic3.items():
    print(k,v)

copy_dic=dic3.copy()
print(copy_dic)

dict1={1:1,2:2}
d=dict(dict1)
print(d)

'''dict={1:1,2:2}
d=dict(dict)
print(d)'''