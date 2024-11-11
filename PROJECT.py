import getpass

Define roles and permissions
ROLES = {
    "admin": ["create", "update", "delete", "view"],
    "user": ["view"]
}

Product class
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock Quantity: {self.stock_quantity}"

Inventory class
class Inventory:
    def __init__(self):
        self.products = {}
        self.users = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def update_product(self, product_id, name=None, category=None, price=None, stock_quantity=None):
        product = self.products.get(product_id)
        if product:
            if name:
                product.name = name
            if category:
                product.category = category
            if price:
                product.price = price
            if stock_quantity:
                product.stock_quantity = stock_quantity
            return True
        return False

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False

    def view_products(self):
        return self.products.values()

    def search_products(self, name=None, category=None):
        results = []
        for product in self.products.values():
            if (name and product.name == name) or (category and product.category == category):
                results.append(product)
        return results

    def filter_products(self, stock_threshold):
        results = []
        for product in self.products.values():
            if product.stock_quantity <= stock_threshold:
                results.append(product)
        return results

    def adjust_stock(self, product_id, quantity):
        product = self.products.get(product_id)
        if product:
            product.stock_quantity += quantity
            return True
        return False

    def add_user(self, username, password, role):
        self.users[username] = {"password": password, "role": role}

    def authenticate(self, username, password):
        user = self.users.get(username)
        if user and user["password"] == password:
            return user["role"]
        return None

def main():
    inventory = Inventory()

    # Initialize admin user
    inventory.add_user("admin", "password", "admin")

    while True:
        print("1. Login")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            role = inventory.authenticate(username, password)

            if role:
                print(f"Welcome, {username} ({role})!")

                if role == "admin":
                    while True:
                        print("1. Add Product")
                        print("2. Update Product")
                        print("3. Delete Product")
                        print("4. View Products")
                        print("5. Search Products")
                        print("6. Filter Products")
                        print("7. Adjust Stock")
                        print("8. Logout")
                        choice = input("Enter your choice: ")

                        if choice == "1":
                            product_id = input("Enter product ID: ")
                            name = input("Enter product name: ")
                            category = input("Enter product category: ")
                            price = float(input("Enter product price: "))
                            stock_quantity = int(input("Enter stock quantity: "))
                            product = Product(product_id, name, category, price, stock_quantity)
                            inventory.add_product(product)
                            print("Product added successfully!")

                        elif choice == "2":
                            product_id = input("Enter product ID: ")
                            name = input("Enter new product name: ")
                            category = input("Enter new product category: ")
                            price = float(input("Enter new product price: "))
                            stock_quantity = int(input("Enter new stock quantity: "))
                            inventory.update_product(product_id, name, category, price, stock_quantity)
                            print("Product updated successfully!")

                        elif choice == "3":
                            product_id = input("Enter product ID: ")
                            inventory.delete_product(product_id)
                            print("Product deleted successfully!")

                        elif choice == "4":
                            products = inventory.view_products()
                            for product in products:
                                print(product)

                        elif choice == "5":
                            name = input("Enter product name: ")
                            category = input("Enter product category: ")
                            products = inventory.search_products(name, category)
                            for product in products:
                                print(product)

                        elif choice == "6":
                            stock_threshold =