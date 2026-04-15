dict={
    "name":"alisha",
    "class":4,
    "roll.no":345
}
print(dict)

#both below methods are same but difference is that in get if element is not there it prints none and does not through error whereas in other it throughs error
print(dict["name"])   
print(dict.keys())
print(dict.get("name7"))  

item=dict["name"]
print(item)

dict["name"]="ANKITA"
print(dict["name"])
#methods to print all keys and values

print(dict.values())
print(dict.keys())
for key1 in dict:
    print(key1)
print(dict.items())

for values,keys in dict.items():
    print({values},{keys}) 

    
#dict methods
ep1={122:45,344:89,78:98}
ep2={45:89,47:848,484:47}
ep1.update(ep2)
print(ep1)
ep1.update({1:7})
print(ep1)

ep1.clear()
print(ep1) #empty dictionary


ep2.pop(45)
print(ep2)


ep2.popitem()
print(ep2)

del ep2 # will delete all the dictionary
    
print(dir(dict))
p=7
print(dir(dict))

class Person:
    def __init__(self, name, age):
         self.name = name
         self.age = age
p1 = Person("John", 30)
print(p1.__dict__)
print(dir(p1))

print(help(Person))

