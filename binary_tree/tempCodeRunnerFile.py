from collections import deque
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def zigzag(root):
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    reverse = False
    
    while queue:
        level_size = len(queue)
        curr_level = []
        for i in range(level_size):
            
            if not reverse:
                curr_node = queue.popleft()
                curr_level.append(curr_node.val)

                if curr_node.left is not None:
                    queue.append(curr_node.left)
                if curr_node.right is not None:
                    queue.append(curr_node.right)
                
            if reverse:
                curr_node = queue.pop()
                curr_level.append(curr_node.val)

                if curr_node.right is not None:
                    queue.appendleft(curr_node.right)
                if curr_node.left is not None:
                    queue.appendleft(curr_node.left)
                    
        result.append(curr_level)    
        reverse = not reverse 
        
    return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(zigzag(root))