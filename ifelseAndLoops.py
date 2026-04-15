#question 1
'''c=int(input("Enter the value of temperature in celsius "))
f=(9/5)*c+32
print("value in farhenheit is ",f,"F")'''

#question 2
'''a=int(input("Enter a number to check to whether it is prime or not"))
  b=1
for i in range(2,a):
 if(a%i==0):
  b=0
if b==1:
 print("Number is prime")
else:
  print("Number is not prime")
'''

'''a=int(input("Enter a number to check to whether it is prime or not"))
for i in range(2,a):
 if(a%i==0):
  print("Number is non prime")
  break
else:
  print("Number is  prime")'''



#question 3
"""age=int(input("Enter a age"))
if age>=18:
 print("You can vote")
else:
 print("You cannot vote")"""
 
#question 4
'''a=int(input("Enter a number to check to whether it is even or not "))
if a%2==0:
 print("Number is even")
elif a==1:
 print("Number is coprime")
else:
 print("Number is odd")
'''

'''#question 5
x=7
match x:
  case 1:
    print("ok")
  case 2:
    print("not done")
  case _:  
    print("hello") '''
    
    
#question 6
'''
a=int(input("Enter a number to find factorial"))
fact=1
def factorial(a):
  if(a==1 or a==0):
    return 1
  else:
   while(a>0):
    fact= a * factorial(a-1)
    return fact
  
result=factorial(a)
print("Result is ",result)

'''

# list=[8,6,3,8,56,9,11,23]
# temp=list[0]
# for values in list:
#     if(values>temp):
#       temp=values
# print("max value is ",temp)


''' #for loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
for i in range( 11):
   print(i,end=' ')

print(" ")
seq=10
for i in range(1, 11):
   print(i**2,end=' ')

print(" ")

for i in range(0,-100,-5):
   print(i,end=' ')

print(" ")


#while loop
i = 1
while i <= 10:
    print(i, end=' ')
    i=i+1'''

#do while loop is not there we can use break and continue for this


#pattern question
'''  1
    1 2
   1 2 3
  1 2 3 4
 1 2 3 4  5 
for i in range(1,7):
  for k in range(7-i):
    print(end=" ")
  for j in range(1,i+1):
   print(j,end=" ")
  print("")'''
  
#for loop with else
'''for i in range(1,4):
  if i==4:
   print("yes")
   break
else:
  print("no")'''


  
  
# def swap():
#    a=7
#    b=6
#    a=a+b
#    b=a-b
#    a=a-b
#    print(a,b)
# swap()

# def area():
#   r=4
#   print("Area is ",3.14*(r**2))
# area()
# #shortend if else statement
# x=56
# y=89
# print(x) if x>y else print(y) if x==y else print(45)
  
# c=7 if x<y else 5
# print(c)


# x = int(input("Enter a number"))

# match x:
#     case 1:
#         print("no")
#     case 2:
#         print("ok")
#     case _ if x > 2:
#         print("done")
#     case _:
#         print("ok")
g=9
if g==9:
  print("hj")
  