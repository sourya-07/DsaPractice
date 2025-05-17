# stack :- Last In First Out (LIFO) data structure.

# syntax to store stack in python
# stack = []             # Create an empty stack

# stack.append(10)       # Push 10 onto the stack
# stack.append(20)       # Push 20 onto the stack

# top = stack.pop()      # Pop the top element (20)










#  Queue :- First In First Out (FIFO) data structure.

# syntax to store queue in python

from collections import deque

queue = deque()         # Create an empty queue

queue.append(10)        # Enqueue 10
queue.append(20)        # Enqueue 20

first = queue.popleft() # Dequeue (removes 10)
