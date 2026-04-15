import numpy as np
arr1=np.array([3,7,7])
print(arr1 *2)

arr2=[3,"Hbn",8]
print(arr2 *2)

#special function in numpy
zero =np.zeros((3,4))
print(zero)


one =np.ones((3,4))
print(one)

full1=np.full((3,5),7)
print(full1)

random1=np.random.random((2,3))
print(random1)

sequence1=np.arange(0,11,2)
print(sequence1)

#matrix 
matrix=np.array([[1,7,8],[7,8,5]])
print(matrix)

tensor1=np.array([[1,32],[22,3],
                  [2,7],[4,3]])
print(tensor1)

print(tensor1.shape)
print(tensor1.ndim)
print(tensor1.size)
print(tensor1.dtype)


tensor4=np.arange(12)
print(tensor4)
print(tensor4.reshape((3,4)))
print(tensor4.flatten())

x=tensor4.reshape((3,4))
print(x)
print(x.T)