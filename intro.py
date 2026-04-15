# print("HELLO !",end="") #end to print in same line 
# print("my name is alisha \n i live in muktsar ")# \n to print in  new line 
# print(3,6,sep="% ")#sep is used to seperate two strings or anythin in print function 

# name="Alisha"
# age=20
# print(age)
# print(name + " " + str(age))

# print("type of age is ",type(age)) #to check data type
# ab=complex(3,4)
# print("complex data type ",ab)
# cla = str(input("Enter your class ")) 
# print(cla)

# print(cla.find('der'))
# print('der' in cla)

# print(6**2)  #to calculate power

# number=range(9)
# print(number)

 #list
# marks=[45,67,56,"fh"]
# print(marks)
# print(marks[-1])
# print(marks[0:3])
# print(type(marks))
# print(len(marks))
 
# if 67 in marks:
#     print("yes")
    
# lst=[i*i for i in range(1,10) ]
# print(lst)

#lst1=[1,23,45] 
# lst1.append(34) #to add element at last in list
# lst1.sort()
# lst1.reverse()
# print(lst1.index(23))
# print(lst1.count(23))
# print(lst1)
# #methods in list# lst1.insert(1,43)
# print(lst1)
# lst1.extend(lst)
# print(lst1)


# '''multiline comments ''' """"this is also a mltiline comment """


# #tuple
# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)
# print(thistuple.count("apple"))s

  
# global variables
# x = 8

# def change():
#     global x
#     print(x)
#     y= x + 5
 
# change()

import random
print(random.randint(0,100))


 #tuple
#tup=(1,4,5) #if you write one element in tuple than , is necessary // difference between list and tuple is that tuple cannot be changed(immutable) whereas list is mutable
# print(type(tup),tup)
# print(tup[-2])
# print(len(tup))
# if 4 in tup:
#  print("yes")
# print(tup[0:2])

# #we cannot change tuple directly first we have to convert it into list
#temp=(2,3,4,5)
# temp=list(temp) #function to change tuple into list
# temp.append(8)
# temp.pop(2)
# temp[2]=7
# temp=tuple(temp)
# print(temp)
# print(temp.index(2))
# print(temp.count(2))


# #we add two tuple

# tup=tup+temp
# print("abc", tup)

#set
# s={1,1,4,6,7,8,3,2} #set cannot take repeated elements
# print(s)
# print(type(s))
# ha={} 

# #set can be empty otherwise it is dicitionary
# print(type(ha)) 
# ha=set()
# print(type(ha)) 

# s1={"new zealand","america","canada"}
# s2={"delhi","muktsar","kotakapura"}
# s3={"america","malout","sinagapur"}

# s1=s1.union(s2)
# print(s1.union(s2))

# s3.update(s1)
# print(s3)

# s3.intersection_update(s1)
# print(s3)

# s3.symmetric_difference(s2)
# print(s2)  #which are present in both will be deleted

# s1.difference(s3)
# print(s1)  #similiar to like A-B

# print(s3.issubset(s1))
# print(s3.issuperset(s2))
# print(s1.isdisjoint(s2))

# s3.add("australlia")
# print(s3)
# s3.remove("delhi")
# print(s3)  #through error when element is not present
# s3.discard("gyh")
# print(s3)  #does not through error when element is not present

# item=s2.pop()
# print(item)

# del s2 #to delete all elements in a set
#from function import *
# from math import sqrt,pi
# result=sqrt(16)
# print(result)
# print(pi)

# import math as m
# print(m.sqrt(8))

# print(dir(m))

#add(6,8)

# foods = list()
# while (food := input("What food do you like?: ")) != "quit":
#        food="hih"
       
       
# import shutil
# # Copying a file
# shutil.copy("jsn.py", "secret.py")
# # Copying a directory
# #shutil.copytree("jsn_dir", "secret_dir")
# # Moving a file
# shutil.move("pdfmerger.py", "pdfmerger.py")
# # Deleting a directory
# #shutil.rmtree("dir")

# import requests
# response = requests.get("https://www.google.com")
# print(response.text)

s="hello     world"
s.strip()
print(s)
nuy=[]
nuy[:]=[2]*1+[3]*3+[7]*3
print(nuy)