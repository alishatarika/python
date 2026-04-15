class hello:
    def __init__(self):
       self.st=[]
    def push(self,x):
        self.st.append(x)
    def pop(self):
        if len(self.st)==0:
            return -1
        x=self.st[-1]
        self.st.pop()
        return x
    def top(self):
        if len(self.st)==0:
            return -1
        return self.st[-1]
    def size(self):
        return len(self.st)
g=hello()
g.push(3)
g.push(7)
print(g.pop())
print(g.top())
print(g.size())
    