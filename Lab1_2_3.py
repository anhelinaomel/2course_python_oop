# Create a class that descibes a Product of online store. As a Product fields you can use a price,
# description and product' dimensions.
# Create a class that describes a Customer. As a Customer fields you can use surname, name, patronymic, mobile phone, etc.
# Create a class that describes an Order - contains data about the customer who carried it out and products.
# Implement a method for calculating the total order value.

class Product:
    def __init__(self, price, description, height, length, width):
        self.price = price
        self.description = description
        self.height = height
        self.length = length
        self.width = width

class Customer:
    def __init__(self, first_name, medium_name, last_name, phone_num):
        self.first_name = first_name
        self.medium_name = medium_name
        self.last_name = last_name
        self.phone_num = phone_num

class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

    def total_value(self):
        sum = 0
        for i in self.products:
            sum += i.price
        return sum


# example 
bear = Product(24.99, "a fluffy Teddy bear", 30, 22, 40)
car = Product(9.99, "a really fast red car", 13, 9, 17)
customer1 = Customer("John", "Junior", "Doe", " 044 204 94 94")

list = []

list.append(bear)
list.append(car)

order = Order(customer1, list)
print(order.total_value())