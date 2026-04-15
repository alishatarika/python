#question 1
fruits=["apple","mango","orange","watermelon","litchi"]
fruits.append("banana")
fruits.pop(1)
fruits.sort()
print(fruits)
fruits=tuple(fruits)
print(fruits)
for i in fruits:
    print(i)
for i in fruits:
    print(i.upper())


# question 2
set={2,6,4,8,3}
set.add(64)
set.remove(8)
print(set)
if 6 in set:
    print("yes")
else:
    print("no")
    

dict={
    "name":"alisha",
    "age":20,
    "city":"muktsar"   
}
dict["age"]=22
dict.update({"profession":"student"})
print(dict)

if dict["age"]<=18:
    print("yes")
else:
    print("older")
    
#question 3
def greet(name):
    print("Hello!",name)
    
name=input("Enter your name")
greet(name)


num=int(input("enter a number "))
print(square(num))

for i in range(1,6):
    print(square(i))