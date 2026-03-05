class Product: 
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    products_list = []
    def add_product(self, name, price):
        self.name = name
        self.price = price
        self.products_list.append((self.name, self.price))

    def show_products(self):
        for product in self.products_list:
            print(f"Product: {product[0]}, Price: {product[1]}")

    def calculate_total(self):
        total = sum(self.price * self.quantity for self in self.products_list)
        return total
    
product1 = Product("Mouse", 5000, 3)
product2 = Product("Keyboard", 8000, 2)

print(product1.calculate_total() + product2.calculate_total()) #34000
