import time

toprint = ["H", 'e', 'l', "l", "o", " ", "W", "o", "r", "l", "d"]
temp = ["","","","","","","","","","",""] 
i = 0
while i < len(toprint):
    if temp[i] != toprint[i]:
        for j in list(range(32, 33)) + list(range(65, 91)) + list(range(97, 123)):
            temp[i] = chr(j)
            print("\n")
            
            print("".join(temp))
            
            if temp[i] == toprint[i]:
                break

    if temp[i] == toprint[i]:
        i =i+1

