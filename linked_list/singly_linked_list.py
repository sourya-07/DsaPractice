# # Create Nodes
# # Create Linkded List
# # Add Nodes to Linkded List 
# # Print Linkded List



# class Node :
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        
        
# class LinkedList :
#     def __init__(self):
#         self.head = None

#     def insert(self, new_node) :
#         # Head => John->None
#         if self.head is None :
#             self.head = new_node
#         else :
#             # self.head.next = new_node
            
#             last_node = self.head
#             while True :
#                 if last_node.next is None :
#                     break
#                 last_node = last_node.next
            
#             last_node.next = new_node
      
            
#     def print_list(self) :
#         # Head => john->Ben->Maxi
        
#         if self.head is None :
#             print("List is empty")
#             return 
            
#         current_node = self.head
#         while True :
#             if current_node is None :
#                 break
#             print(current_node.data)
#             current_node = current_node.next 
        
        


# #  Node => data, next 
# # firstNode.data => John, firstNode.next => None.
# firstNode = Node("John")
# linkedList = LinkedList()
# linkedList.insert(firstNode)

# secondNode = Node("Ben")
# linkedList.insert(secondNode)

# thirdNode = Node("Maxi")
# linkedList.insert(thirdNode)

# # Calling the print_list function so that it can print linked list.
# linkedList.print_list()



















class Dog() :
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        
        
    def add_friend(self, friend_name) :
        self.friend = friend_name
        
        
    def print_name(self) :
        print("My name is" + self.name)
        
        

simba = Dog("Simba", 1, "Husky")
stella = Dog("Stella", 3, "G.R.")
leo = Dog("Leo", 2, "L.R")
strom = Dog("Strom", 3, "Indian")

