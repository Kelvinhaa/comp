class TreeNode:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self): #Visit the far left and print the smallest first
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()
    
    def preorder_traversal(self): #print nodes first before going far left
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self): #print deepest node from left to right
        
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)
    
    def find(self, value):
        if value < self.value:
            if not self.left:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if not self.right:
                return False
            else:
                return self.right.find(value)
            
        else:
            return True
        

if __name__ == "__main__":
    tree = TreeNode(6)
    tree.insert(5)
    tree.insert(7)
    tree.insert(10)
    tree.insert(9)
    tree.insert(11)
    tree.insert(20)
    
    tree.inorder_traversal()
    print(tree.find(30))