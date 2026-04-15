arr=[2,5,4,7,8]
n=len(arr)
for i in range(0,n):
    swapped = False
    for j in range(i,n-i-1):
        if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  
        
print(arr)