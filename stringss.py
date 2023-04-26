#Slicing

string="championships"
print(string[0:5])
print(string[5:8])
print(string[-5:-1])
print(string[:3])
print(string[3:])


#String interpolation

pie=3.14
print(f"the string is {pie} is")

age =10
years=40

hello="in {} years i will be {}"
print(hello.format(age ,years))