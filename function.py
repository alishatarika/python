def add(a,b):
     '''add to numbers'''
     print("Your result is ",a+b)

if __name__ == "__main__":
 add(7,8)
print(add.__doc__) 


#docstring is to print cooments inside any functions
# #pass when you only declare a function and want to define later

a=5
print(f"your value is {a}")

# def fibonacci_series(n):
#     if n == 0:
#         print(0)
#         return
#     elif n == 1:
#         print(0, 1)
#         return

#     n0, n1 = 0, 1
#     print(n0, n1, end=" ")

#     for i in range(2, n):
#         n0, n1 = n1, n0 + n1
#         print(n1, end=" ")

# # Example usage:
# fibonacci_series(5)

#enumerate function  it is use dto get the index and value in a list and tuple at the same time
# num={4,9,2,0,6,8}
# for index,nums in enumerate(num):
    
#     if index==2:
#         print("Great")

#     else:
#         print(nums) 
        
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")

def abc(**kwarg):
     print(kwarg["name"])

abc(name="Pratik", age="28")

squ = lambda x:x**2
print(squ(3))

squ = lambda x,y,z:(x+y+z)/2
print(squ(1,2,3))


#map
def cube(x):
     return x*x*x

lis=(1,5,2,7,9)
newl=list(map(cube,lis))
print(newl)

#filter
def filter_function(a):
     return a>4
newl2=list(filter(filter_function,newl))
print(newl2)

#reduce
from functools import reduce
numbers=[4,6,2,8,1,7]

def sum(x,y):
     return x+y
sum1=reduce(sum,numbers)
print(sum1)
