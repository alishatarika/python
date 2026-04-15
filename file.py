# f=open('fil.txt','w')
# f.write(input("Enter a msg"))
# f.close()


f=open('fil.txt','a')
f.write('My name is alisha \n')
f.close()

with open('fil.txt', 'a') as f:
    f.write("Done \n")

f=open('fil.txt','r')
txt=f.read()
print(txt)
f.close()

f=open('fil.txt','r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)


f = open('fil.txt', 'a')
lines = input("Enter a msg")
for line in lines:
 if line=='.':
    f.write('\n')
 else:  
  f.writelines(line)
f.close()

with open('fil.txt', 'r') as f:
    f.seek(2)
    data=f.read()
print(data)

with open('fil.txt', 'r') as f:
  data = f.read(10)
  current_position = f.tell()
  f.seek(current_position)
print(current_position)

with open('fil.txt', 'w') as f:
  f.write("hello world")
  f.truncate(5)
with open('fil.txt', 'r') as f:
  print(f.read())