# How to create Class
class Item:
    def calculate_total_price(self, x, y):
        return x * y


# How to create an instance of a class
item1 = Item()

# Assign attributes
item1.name = 'Phone'
item1.price = 1000
item1.quantity = 5

# Calling methods from instances of a class:
print(item1.calculate_total_price(item1.price, item1.quantity))