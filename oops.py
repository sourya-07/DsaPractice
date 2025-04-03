# How to create Methods in a class :-

# class Item :
#     def calculate_total_price(self, x, y):
#         return x * y


# item1 = Item()
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))

# item2 = Item()
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 5

# print(item2.calculate_total_price(item2.price, item2.quantity))







class Item :
    def __init__(self, name: str, price, quantity):
        
        assert price >= 0 
        assert quantity >= 0 
        
        
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 10000, 100)

item2 = Item("Keshav", 100000, 50)


# print(item1.name, item1.quantity)
# print(item1.price)
# print(item1.quantity)

# print(item2.name)
# print(item2.price)
# print(item2.quantity)


print(item1.calculate_total_price())
print(item2.calculate_total_price())








