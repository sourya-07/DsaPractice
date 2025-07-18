# Preorder Traversal:-
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def preorderTraversal(self, root):
#         def helper(node, result):
#             if not node:
#                 return
#             result.append(node.val)
#             helper(node.left, result)
#             helper(node.right, result)
        
#         result = []
#         helper(root, result)
#         return result





# Inorder Traversal:- 

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root):
        
#         if root is None :
#             return []
        
#         left = self.inorderTraversal(root.left)
#         right = self.inorderTraversal(root.right)
#         curr = [root.val]

#         return left + curr + right









# Post order Traversal:-

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def postorderTraversal(self, root):
        
#         if root is None:
#             return []
        
#         left = self.postorderTraversal(root.left)
#         right = self.postorderTraversal(root.right)
#         curr = [root.val]

#         return left + right + curr