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










# Array Implementation of Queue :-

# class Queue :
#     def __init__(self) :
#         self.q = []
#         self.front = -1
        
#     def push(self, x) :
#         if self.front == -1 :
#             self.front = 0
        
#         self.q.append(x)
        
#     def pop(self):
#         if len(self.q) == 0 :
#             return -1
#         x = self.q[self.front]
#         self.front += 1
#         if self.front == len(self.q) :
#             self.front = -1
#             self.q = []
        
#         return x
    
#     def getFront(self) :
#         if len(self.q) == 0:
#             return -1
#         return self.q[self.front]
    
#     def size(self):
#         if self.front == -1 :
#             return 0
#         return len(self.q) - self.front
    
    
    
# queue = Queue()
# queue.push(5)
# queue.push(4)
# queue.push(3)
# queue.push(1)

# print(queue.getFront())
# queue.pop()
# print(queue.getFront())

# print(queue.size())








# Linked List Implementation of Queue :-


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#         self.length = 0
        
#     def push(self, x) :
#         newNode = Node(x)
#         self.length += 1
#         if self.front is None:
#             self.front = newNode
#             self.rear = newNode
            
#         else:  
#             self.rear.next = newNode
#             self.rear = newNode
            
#     def pop(self):
#         if self.front is None:
#             return -1
        
#         x = self.front.data
#         self.front = self.front.next
#         self.length -= 1
#         if self.front is None:
#             self.rear = None
            
#         return x
    

#     def getFront(self) :
#         if self.front is None:
#             return -1
        
#         return self.front.data
    
#     def size(self) :
#         return self.length
    

# queue = Queue()
# queue.push(1)
# queue.push(4)
# queue.push(3)
# queue.push(1)

# print(queue.getFront())
# queue.pop()
# print(queue.getFront())
# print(queue.size())








# Remove Outermost Parentheses with 2 approch



def removeOuterParentheses(s):
    
    # stack, res = [], ''
    # for i in range(len(s)):
    #     if s[i] == '(':
    #         if stack:
    #             res += '('
    #         stack.append(s[i])
        
    #     else :
    #         stack.pop()
    #         if stack:
    #             res += ')'
    
    # return res

    res, c = '', 0

    for i in range(len(s)) :
        if s[i] == '(':
            if c > 0 :
                res += '('
            c += 1
        else :
            c -= 1
            if c > 0:
                res += ')'
    
    return res


print(removeOuterParentheses("((()()()))(())"))