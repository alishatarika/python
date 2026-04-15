l=[1,3,5,6]
search=5
for i in range(0,len(l)):
    if l[i] ==search:
        print("got")
mid=len(l)//2
left = 0
right = len(l) - 1

while left <= right:
    mid = (left + right) // 2

    if l[mid] == search:
      print("found")

    if l[mid] < search:
      left = mid + 1
    else:
      right = mid - 1

    