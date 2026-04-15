class node1:
    def __init__(self,value):
        self.value =value
        self.next=None
a=node1(6)
b=node1(8)
c=node1(4)
a.next=b
b.next=c
front=a
print(front.value)
print(front.next.value)
print(front.next.next.value)
#traverse a linked list
while front !=None:
    print(front.value,end=" ")
    front=front.next
#insertion at the begining and last
r=node1(5)
r.next=a
front=r
t=node1(3)
while a.next !=None:
    a=a.next
a.next=t
front=r
while front !=None:
    print(front.value,end=" ")
    front=front.next
    
    
print("insertion at kth")
#insertion at the kth position
new =node1(11122)
front=r
k=2
for i in range(k-1):
    front=front.next
new.next=front.next
front.next=new
front=r
#to delete front begining
#front=front.next
while front !=None:
    print(front.value,end=" ")
    front=front.next
front=r
print("\n")
while front.next !=None:
    print(front.value,end=" ")
    front=front.next
front=r
for i in range(k-1):
    front=front.next
front.next=front.next.next
front=r
while front !=None:
    print(front.value,end=" ")
    front=front.next
front=r
