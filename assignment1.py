# Question 1
'''
i=int(input("Enter a number you want to print table "))
print(f"Table of {i} is ")
for j in range(1,11):
    print(f"Table of {i} X {j} = {i*j}") 
'''    
     

#question 2    
'''
for i in range (1,51):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)
'''

#question 3
'''
for i in range (1,21):
    if(i%4==0):
      continue
    print(i)
  
'''

#question 5

#i=int(input("Enter a number"))
temp=7
r=0
while i>0:
   n=i%10
   r=r*10+n
   i=int(i/10)

if(r==temp):
    print("Number is palindrome")
else:
    print("Number is not palindrome")

'''
#question 6  
i=int(input("Enter a number"))
temp=i
r=0
while i>0:
   n=i%10
   r=r*10+n
   i=int(i/10)
    
print(r)
'''