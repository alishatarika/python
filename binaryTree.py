class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    
head=Tree(5)
head.left=Tree(4)
head.right=Tree(5)
head.left.right=Tree(5)