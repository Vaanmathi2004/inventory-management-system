class Product:
    '''
    Product class to store product details.

    Attributes:
    product_id (int): Unique identifier for the product.
    name (str): Name of the product.
    price (float): Price of the product.
    quantity (int): Quantity of the product in stock.

    '''
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class InventoryManagementSystem:
    '''
    Inventory Management System class to manage products in inventory.

    Attributes:
    inventory (dict): A dictionary to store product_id and Product object.
    total_revenue (float): Total revenue from sales.

    Methods:
    add_product: Add a new product to the inventory.
    update_product: Update an existing product in the inventory.
    track_inventory: Track products with low stock based on a threshold quantity.
    record_sale: Record a sale of a product and update the inventory.
    generate_report: Generate a report of the current inventory and total revenue.

    '''

    def __init__(self):
        self.inventory = {}
        self.total_revenue = 0

    def add_product(self, product_id, name, price, quantity):
        '''
        Add a new product to the inventory.

        Args:
        product_id (int): Unique identifier for the product.
        name (str): Name of the product.
        price (float): Price of the product.
        quantity (int): Quantity of the product in stock.

        '''
        if product_id in self.inventory:
            print("Product ID already exists.")
            update_option = input("Do you want to update this product? (yes/no): ").lower()
            if update_option == "yes":
                self.update_product(product_id, name, price, quantity)
            else:
                return
        else:
            self.inventory[product_id] = Product(product_id, name, price, quantity)
            print("Product added successfully.")

    def update_product(self, product_id, name=None, price=None, quantity=None):
        '''
        Update an existing product in the inventory.

        Args:
        product_id (int): Unique identifier for the product.
        name (str): New name of the product (optional).
        price (float): New price of the product (optional).
        quantity (int): New quantity of the product in stock (optional).

        '''
        if product_id in self.inventory:
            if name:
                self.inventory[product_id].name = name
            if price is not None:
                self.inventory[product_id].price = float(price)
            if quantity is not None:
                self.inventory[product_id].quantity = int(quantity)
            print("Product updated successfully.")
        else:
            print("Product ID does not exist.")

    def track_inventory(self, threshold):
        '''
        Track products with low stock based on a threshold quantity.

        Args:
        threshold (int): Threshold quantity to identify low stock products.

        Returns:
        list: List of Product objects with low stock.

        '''

        low_stock_products = []
        for product in self.inventory.values():
            if product.quantity < threshold:
                low_stock_products.append(product)
        if not low_stock_products:
            print("No low stock products.")
            return
        return low_stock_products

    def record_sale(self, product_id, quantity_sold):
        '''
        Record a sale of a product and update the inventory.

        Args:
        product_id (int): Unique identifier for the product.
        quantity_sold (int): Quantity of the product sold.

        '''
        if product_id in self.inventory:
            if quantity_sold <= 0:
                print("Invalid sale quantity.")
            elif self.inventory[product_id].quantity >= quantity_sold:
                self.inventory[product_id].quantity -= quantity_sold
                self.total_revenue += self.inventory[product_id].price * quantity_sold
                print("Sale recorded successfully.")
            else:
                print("Insufficient stock.")
        else:
            print("Product ID does not exist.")

    def generate_report(self):
        '''
        Generate a report of the current inventory and total revenue.

        '''
        if not self.inventory:
            print("No products in inventory.")
            return
        print("Current Inventory:")
        for product in self.inventory.values():
            print(f"Product: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
        print(f"Total Revenue from Sales: Rs.{self.total_revenue}")

# Create an instance of the InventoryManagementSystem
inventory_system = InventoryManagementSystem()

def add_product_input():
    '''
    Function to take user input for adding a new product to the inventory.

    '''

    while True:
        try:
            product_id = int(input("Enter Product ID: "))
            if product_id < 0:
                print("Product ID cannot be negative. Please enter a positive integer for Product ID.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for Product ID.")

    if product_id in inventory_system.inventory:
        print("Product ID already exists.")
        update_option = input("Do you want to update this product? (yes/no): ").lower()
        if update_option == "yes":
            update_product_input(product_id)
        return

    name = input("Enter Product Name: ")
    while True:
        try:
            price = float(input("Enter Product Price: "))
            if price < 0:
                print("Price cannot be negative. Please enter a positive number for Product Price.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for Product Price.")

    while True:
        try:
            quantity = int(input("Enter Product Quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please enter a positive integer for Product Quantity.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for Product Quantity.")

    inventory_system.add_product(product_id, name, price, quantity)

def update_product_input(product_id):
    '''
    Function to take user input for updating an existing product in the inventory.
    '''
    if product_id not in inventory_system.inventory:
        print("Product ID does not exist.")
        return

    name = input("Enter New Product Name (Leave blank to keep current): ")

    while True:
        price = input("Enter New Product Price (Leave blank to keep current): ")
        if price:
            try:
                price = float(price)
                if price < 0:
                    print("Price cannot be negative. Please enter a positive number for Product Price.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number for Product Price.")
                continue
        else:
            price = None
        break

    while True:
        quantity = input("Enter New Product Quantity (Leave blank to keep current): ")
        if quantity:
            try:
                quantity = int(quantity)
                if quantity < 0:
                    print("Quantity cannot be negative. Please enter a positive integer for Product Quantity.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid integer for Product Quantity.")
                continue
        else:
            quantity = None
        break

    inventory_system.update_product(product_id, name, price, quantity)

def record_sale_input():
    '''
    Function to take user input for recording a sale of a product.
    '''
    while True:
        try:
            product_id = int(input("Enter Product ID to Record Sale: "))
            if product_id < 0:
                print("Product ID cannot be negative. Please enter a positive integer for Product ID.")
                continue
            quantity_sold = int(input("Enter Quantity Sold: "))
            if quantity_sold <= 0:
                print("Quantity sold must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter valid integers.")
    inventory_system.record_sale(product_id, quantity_sold)

def track_inventory_input():
    '''
    Function to take user input for tracking low stock products based on a threshold quantity.
    '''
    while True:
        try:
            threshold = int(input("Enter Threshold Quantity: "))
            if threshold < 0:
                print("Threshold quantity cannot be negative. Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    low_stock = inventory_system.track_inventory(threshold)
    if low_stock:
        print("Low stock products:")
        for product in low_stock:
            print(f"{product.name}: {product.quantity}")


# Main program loop

while True:
    print("\n=== Inventory Management System ===")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Record Sale")
    print("4. Track Low Stock Products")
    print("5. Generate Report")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_product_input()
    elif choice == '2':
        while True:
            try:
                product_id = int(input("Enter Product ID to Update: "))
                if product_id < 0:
                    print("Product ID cannot be negative. Please enter a positive integer for Product ID.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for Product ID.")
        update_product_input(product_id)
    elif choice == '3':
        record_sale_input()
    elif choice == '4':
        track_inventory_input()
    elif choice == '5':
        inventory_system.generate_report()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
