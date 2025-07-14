# # BFS:- by kunal khuswaha
# from collections import deque

# class Node:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
# def bfs(root):
#     result = []
    
#     if root is None:
#         return result
    
#     queue = deque()
#     queue.append(root)
    
#     while queue:
#         level_size = len(queue)
#         curr_level = []
#         for i in range(level_size):
#             curr_node = queue.popleft()
#             curr_level.append(curr_node.val)
            
#             if curr_node.left is not None:
#                 queue.append(curr_node.left)
#             if curr_node.right is not None:
#                 queue.append(curr_node.right)
            
#         result.append(curr_level)
    
#     return result

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)
# print(bfs(root))








# Level order Successor of a node:-

from collections import deque
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def bfs(root, k):
    
    if root is None:
        return None
    queue = deque()
    queue.append(root)
    
    while queue:
        curr_node = queue.popleft()
        
        if curr_node.left is not None:
            queue.append(curr_node.left)
        if curr_node.right is not None:
            queue.append(curr_node.right)
        
        if curr_node.val == k:
            break
    
    if queue: return queue[0]
    else: return None
    
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

successor = bfs(root, 2)
if successor:
    print(successor.val)  # Output should be 3
else:
    print("No successor found")