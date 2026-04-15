import numpy as np

list=[]
for i in range(0,10):
    list.append(i)
arr1=np.array(list)
print(arr1)
square=[i*i for i in list ]
squ=np.array(square)
print(squ)

arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr[1:6])
print(arr[-3:])
print(arr[0:10:2])

a=np.array([1,2,3,4,5])
b=np.array([5,4,3,2,1])
addition=a+b
print(addition)
multiplication=a*b
print(multiplication)
dot=np.dot(a,b)
print(dot)

num=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
num=num.reshape((3,4))
print(num[0])

arr2=np.array([10,15,20,25,30,35,40])
boolarr2=arr2>20
print(arr2[boolarr2])

num1=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
num1=num1.reshape((3,3))
print(num1)

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
transposed_array = array_2d.transpose()
print(transposed_array)

num2=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9,10])
sum=num2.sum()
mean=num2.mean()
print("sum is ",sum)
print("meam is ",mean)

a1=np.array([1,2,3])
b1=np.array([4,5,6])
add=a1+b1
sub=a1-b1
multi=a1*b1
print(add)
print(sub)
print(multi)

new=np.concatenate((a1,b1))
print(new)
print(np.sort(a))
s=np.where(a1==2)
print(s)
