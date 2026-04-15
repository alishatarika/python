array=[4,2,6,3,8]
for i in range(0,len(array)):
    min=i
    for j in range(i+1,len(array)):
        if array[j]<array[min]:
            min=j
    array[i], array[min] = array[min], array[i]
print(array)