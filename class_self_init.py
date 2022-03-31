
class animal:
    leg=4
    def printdetails(self):
        return f"{self.name} is {self.type} animal its color {self.clr}."

dog=animal()
cow=animal()
cat=animal()

cow.name="cow"
cow.type="milky"
cow.clr="brown"

dog.name="dog"
dog.type="domestic"
dog.clr="black"

cat.name="cat"
cat.type="domestic"
cat.clr="black"


print("dog :",dog.leg)
print("cow :",cow.leg)
print(cow.printdetails())
print()

dog.leg=3
cow.leg=5

print("dog :",dog.leg)
print("cow :",cow.leg)
print("cat :",cat.leg)
print()

animal.leg=9

print("after change:")
print("dog :",dog.leg)
print("cow :",cow.leg)
print("cat :",cat.leg)

#print(dog.printdetails())

