'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def addNumber(first, second): 

    dummy = Node(0)
    curr = dummy

    carry = 0
    while first or second or carry :

        if first :
            v1 = first.data 
        else :
            v1 = 0

        if second :
            v2 = second.data
        else :
            v2 = 0

        
        value = v1 + v2 + carry
        carry = value // 10
        value = value % 10

        curr.next = Node(value)
        curr = curr.next

        if first :
            first = first.next

        if second :
            second = second.next

    
    return dummy.next