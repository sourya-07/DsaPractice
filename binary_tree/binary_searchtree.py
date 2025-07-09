# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.height = 1

#     def insert(self, value):
#         if value < self.value:
#             if self.left:
#                 self.left.insert(value)
#             else:
#                 self.left = BST(value)
#         else:
#             if self.right:
#                 self.right.insert(value)
#             else:
#                 self.right = BST(value)

#     def getValue(self):
#         return self.value

#     def inorder(self):
#         if self.left:
#             self.left.inorder()
#         print(self.value, end=' ')
#         if self.right:
#             self.right.inorder()


# root = BST(10)
# root.insert(5)
# root.insert(15)
# root.insert(6)
# root.insert(7)

# print("Inorder traversal:")
# root.inorder()  # Output: 5 7 10 15





class TreeNode:
    
    def __init__(self, value):
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

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value)
        if self.right:
            self.right.inorder()
    
    
    def preorder(self):
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value)
    
    
tree = TreeNode.insert(5)
