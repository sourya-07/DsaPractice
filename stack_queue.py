# Array Implementation of Stack:-

# stack = []
# stack.append(8)
# stack.append(1)
# stack.append(3)
# stack.append(4)

# print(stack)
# stack.pop()
# print(stack)



# class Stack:
#     def __init__(self):
#         self.st = []
        
#     def push(self, x):
#         self.st.append(x)
    
#     def pop(self) :
#         if len(self.st) == 0 :
#             return -1     
#         x = self.st[-1]
#         self.st.pop()
#         return x
    
#     def top(self):
#         if len(self.st) == 0:
#             return -1
#         return self.st[-1]

#     def size(self) :
#         return len(self.st)
    

# stack = Stack()
# stack.push(5)
# stack.push(4)
# stack.push(3)
# stack.push(9)

# print(stack.pop())
# print(stack.pop())
# print(stack.size())








# Linked List Implementation of Stack :-

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.length = 0
        
#     def push(self, x) :
#         self.length += 1
#         if self.top is None :
#             top = Node(x)
#             return 
#         else :
#             newNode = Node(x)
#             newNode.next = self.top
#             top = newNode
            
#     def pop(self):
#         if self.top == None :
#             return -1
#         self.length -= 1
#         x = self.top.data
#         self.top = self.top.next
#         return x
    
#     def getTop(self) :
#         if self.top == None :
#             return -1
#         return self.top.data
    
#     def size(self):
#         return self.length